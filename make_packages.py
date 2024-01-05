#!/usr/bin/env python3

# https://developers.google.com/protocol-buffers/docs/pythontutorial
# https://blog.conan.io/2019/03/06/Serializing-your-data-with-Protobuf.html

import os, sys, shutil
import binascii

from google.protobuf import text_format
import google.protobuf.message

import resource.liveupdate_ddf_pb2

BUILDERS = {}
BUILDERS['.dmanifest']      = resource.liveupdate_ddf_pb2.ManifestFile
BUILDERS['.dmanifestdata']  = resource.liveupdate_ddf_pb2.ManifestData

def print_dmanifest(manifest_file):
    for field, data in manifest_file.ListFields():
        if field.name == 'data':
            t = resource.liveupdate_ddf_pb2.ManifestData()
            t.MergeFromString(data)
            print(field.name, ":")
            print(t)

        else:
            print(field.name, ":", data)

def text_printer(obj):
    out = text_format.MessageToString(obj)
    print(out)

PRINTERS = {}
PRINTERS['.dmanifest']  = print_dmanifest


common = [
  "/main/common/common.collectionc",
  "/main/common/common.texturec",
  "/_generated_a5475102567b9d0a.goc",
  "/_generated_381894f48195a3ec.spritec",
  "/main/common/common.a.texturesetc",
  ]

level1 = [
  "/_generated_c36c1701ac78b062.spritec",
  "/builtins/fonts/label-df.materialc",
  "/_generated_4a49d953d23621e6.goc",
  "/main/common/common.texturec",
  "/main/level1/level1.a.texturesetc",
  "/_generated_a5475102567b9d0a.goc",
  "/_generated_381894f48195a3ec.spritec",
  "/main/level1/level1.collectionc",
  "/builtins/fonts/font-df.materialc",
  "/builtins/materials/sprite.vpc",
  "/builtins/fonts/font-df.vpc",
  "/main/level1/level1.texturec",
  "/builtins/materials/sprite.materialc",
  "/_generated_96a4af3d0d2fae57.labelc",
  "/main/common/common.collectionc",
  "/dirtylarry/larryfont.fontc",
  "/main/common/common.a.texturesetc",
  "/builtins/materials/sprite.fpc",
  "/builtins/fonts/font-df.fpc",
  ]

level2 = [
  "/builtins/fonts/label-df.materialc",
  "/main/level2/level2.collectionc",
  "/_generated_680bb78e68208171.spritec",
  "/_generated_69c9eb884035dc2d.goc",
  "/main/level2/level2.a.texturesetc",
  "/builtins/fonts/font-df.materialc",
  "/builtins/materials/sprite.vpc",
  "/builtins/fonts/font-df.vpc",
  "/_generated_214aaa84bdb20eda.goc",
  "/main/level2/level2.scriptc",
  "/builtins/materials/sprite.materialc",
  "/_generated_dda0a05c7bdc0a3a.goc",
  "/dirtylarry/larryfont.fontc",
  "/_generated_bad75e846782cc82.labelc",
  "/main/base/base.labelc",
  "/_generated_e35f9efbb90ec201.collectionproxyc",
  "/builtins/materials/sprite.fpc",
  "/main/level2/level2.texturec",
  "/builtins/fonts/font-df.fpc",
  ]

level3 = [
  "/main/level3/level3.collectionc",
  "/builtins/fonts/label-df.materialc",
  "/main/common/common.texturec",
  "/_generated_a5475102567b9d0a.goc",
  "/main/level3/level3.a.texturesetc",
  "/main/level3/level3.texturec",
  "/_generated_381894f48195a3ec.spritec",
  "/_generated_27496cc10a86d50c.goc",
  "/_generated_df771096bf38384b.spritec",
  "/main/level3/level3.scriptc",
  "/builtins/fonts/font-df.materialc",
  "/builtins/materials/sprite.vpc",
  "/builtins/fonts/font-df.vpc",
  "/builtins/materials/sprite.materialc",
  "/_generated_18676589047b8e89.goc",
  "/_generated_dfc36d9e705954af.collectionfactoryc",
  "/main/common/common.collectionc",
  "/dirtylarry/larryfont.fontc",
  "/_generated_56fa200a5617a61d.labelc",
  "/main/common/common.a.texturesetc",
  "/builtins/materials/sprite.fpc",
  "/builtins/fonts/font-df.fpc",
  ]

common_file = 'defold.resourcepack_x86_64-macos_common.zip'
level1_file = 'defold.resourcepack_x86_64-macos_level1.zip'
level2_file = 'defold.resourcepack_x86_64-macos_level2.zip'
level3_file = 'defold.resourcepack_x86_64-macos_level3.zip'

def load_file(path):
    _, ext = os.path.splitext(path)
    builder = BUILDERS.get(ext, None)
    if builder is None:
        print("No builder registered for filetype %s" %ext)
        sys.exit(1)

    with open(path, 'rb') as f:
        content = f.read()
        obj = builder()
        obj.ParseFromString(content)
    return obj

def write_manifest_data(manifest_file, path):
    t = resource.liveupdate_ddf_pb2.ManifestData()
    t.MergeFromString(manifest_file.data)
    with open(path, 'wb') as f:
        f.write(text_format.MessageToString(t, as_utf8=True).encode('utf-8'))
        print("Wrote", path)


def create_manifest(manifest, files):
    pass
    # for field, data in manifest_file.ListFields():
    #     if field.name == 'data':
    #         t = resource.liveupdate_ddf_pb2.ManifestData()
    #         t.MergeFromString(data)
    #         print(field.name, ":")
    #         print(t)

    #     else:
    #         print(field.name, ":", data)

def prune_resources(resources, expected_resources):
    kept = []
    for x in resources:
        if x.url in expected_resources:
            if x.flags == 2:
                print("  KEPT", x.url)
                kept.append(x)
    return kept

def copy(src, tgt):
    shutil.copy2(src, tgt)
    print("Copied", src, "->", tgt)

def create_zip(build_dir, resources, manifest_path, out_zip_path):
    tmpdir = os.path.normpath(os.path.join(build_dir, "./zipdir"))
    if os.path.isdir(tmpdir):
        print("Temp dir already existed! Removing", tmpdir)
        shutil.rmtree(tmpdir)

    os.makedirs(tmpdir)
    #print("Created", tmpdir)

    copy(manifest_path, os.path.join(tmpdir, "liveupdate.game.dmanifest"))

    for x in resources:
        name = binascii.hexlify(x.hash.data).decode('ascii')
        url = x.url
        if url[0] == '/':
            url = url[1:]

        copy(os.path.join(build_dir, url), os.path.join(tmpdir, name))

    zippath = os.path.abspath(out_zip_path)
    oldcwd = os.getcwd()
    os.chdir(tmpdir)
    try:
        os.system('zip %s *' % zippath)
        print("Wrote", zippath)
    finally:
        os.chdir(oldcwd)

    shutil.rmtree(tmpdir)
    #print("Removed", tmpdir)


if __name__ == '__main__':

    manifestdata_path = "./tmp/liveupdate.game.dmanifestdata"
    manifest_path = sys.argv[1]
    # write_manifest_data(manifest, "./tmp/liveupdate.game.dmanifestdata")

    packages = [
        ("common", common),
        ("level1", level1),
        ("level2", level2),
        ("level3", level3),
    ]

    platform = "x86_64-macos"
    for name, resources in packages:
        manifest = load_file(manifest_path)

        manifestdata = resource.liveupdate_ddf_pb2.ManifestData()
        manifestdata.MergeFromString(manifest.data)

        print(name)
        kept_resources = prune_resources(manifestdata.resources, resources)
        manifestdata.resources.clear()
        manifestdata.resources.extend(kept_resources)

        manifest.data = manifestdata.SerializeToString()

        out_manifest_path = "./tmp/defold.resourcepack_%s_%s.dmanifest" % (platform, name)
        out_manifestdata_path = "./tmp/defold.resourcepack_%s_%s.dmanifestdata" % (platform, name)
        out_zip_path = "./build/zips/defold.resourcepack_%s_%s.zip" % (platform, name)

        #print_dmanifest(manifest)
        # print("data")
        # print(manifest.data)

        with open(out_manifest_path, 'wb') as f:
            f.write(manifest.SerializeToString())
            print("Wrote", out_manifest_path)

        with open(out_manifestdata_path, 'wb') as f:
            f.write(text_format.MessageToString(manifestdata).encode('utf-8'))
            print("Wrote", out_manifestdata_path)

        build_dir = "./build/default"
        create_zip(build_dir, kept_resources, out_manifest_path, out_zip_path)
