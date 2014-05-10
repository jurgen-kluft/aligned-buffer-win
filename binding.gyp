{
  "targets": [
    {
      "target_name": "aligned_buffer",
      "sources": [
        "src/aligned-buffer.cc"
      ],
      'conditions': [
        [ 'OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': ['-O2']
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': ['-O2']
          }
        }],
        [
          "OS=='win'",
          {
              "link_settings": {
                  "libraries": [
                      
                  ]
              },
              "configurations": {
                  "Debug": {
                      "msvs_settings": {
                          "VCCLCompilerTool": {
                              "ExceptionHandling": "0",
                              "AdditionalOptions": [
                                  "/MP /EHsc"
                              ]
                          },
                          "VCLibrarianTool": {
                              "AdditionalOptions": [
                                  "/LTCG"
                              ]
                          },
                          "VCLinkerTool": {
                              "LinkTimeCodeGeneration": 1,
                              "LinkIncremental": 1,
                              "AdditionalLibraryDirectories": [
                                  
                              ]
                          }
                      }
                  },
                  "Release": {
                      "msvs_settings": {
                          "VCCLCompilerTool": {
                              "RuntimeLibrary": 0,
                              "Optimization": 3,
                              "FavorSizeOrSpeed": 1,
                              "InlineFunctionExpansion": 2,
                              "WholeProgramOptimization": "true",
                              "OmitFramePointers": "true",
                              "EnableFunctionLevelLinking": "true",
                              "EnableIntrinsicFunctions": "true",
                              "RuntimeTypeInfo": "false",
                              "ExceptionHandling": "0",
                              "AdditionalOptions": [
                                  "/MP /EHsc"
                              ]
                          },
                          "VCLibrarianTool": {
                              "AdditionalOptions": [
                                  "/LTCG"
                              ]
                          },
                          "VCLinkerTool": {
                              "LinkTimeCodeGeneration": 1,
                              "OptimizeReferences": 2,
                              "EnableCOMDATFolding": 2,
                              "LinkIncremental": 1,
                              "AdditionalLibraryDirectories": [
                                  
                              ]
                          }
                      }
                  }
              }
          }
        ]
      ]
    }
  ]
}