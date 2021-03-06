from tap_kit.streams import Stream


class ProspectsStream(Stream):

    stream = 'prospects'

    meta_fields = dict(
        key_properties=['id'],
        replication_key='updatedAt',
        valid_replication_keys=['updatedAt'],
        incremental_search_key=['start_time'],
        replication_method='incremental',
        selected_by_default=False
    )
    schema = \
{
  "type": "object",
  "properties": {
    "relationships": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "account": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            }
          }
        },
        "persona": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null"
              ]
            }
          }
        },
        "calls": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "links": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "related": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        },
        "creator": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            }
          }
        },
        "tasks": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "links": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "related": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        },
        "mailings": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "links": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "related": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        },
        "phoneNumbers": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "meta": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "count": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            },
            "links": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "related": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            },
            "data": {
              "type": [
                "null",
                "array"
              ],
              "items": {
                "type": [
                  "null",
                  "object"
                ],
                "properties": {
                  "type": {
                    "type": [
                      "null",
                      "string"
                    ]
                  },
                  "id": {
                    "type": [
                      "null",
                      "integer"
                    ]
                  }
                }
              }
            }
          }
        },
        "sequenceStates": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "links": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "related": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        },
        "updater": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            }
          }
        },
        "owner": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            }
          }
        },
        "stage": {
          "type": [
            "null",
            "object"
          ],
          "properties": {
            "data": {
              "type": [
                "null",
                "object"
              ],
              "properties": {
                "type": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "id": {
                  "type": [
                    "null",
                    "integer"
                  ]
                }
              }
            }
          }
        }
      }
    },
    "attributes": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "addedAt": {
          "type": [
            "null"
          ]
        },
        "engagedScore": {
          "type": [
            "null",
            "number"
          ]
        },
        "updatedAt": {
          "type": [
            "null",
            "string"
          ]
        },
        "externalSource": {
          "type": [
            "null",
            "string"
          ]
        },
        "occupation": {
          "type": [
            "null"
          ]
        },
        "title": {
          "type": [
            "null",
            "string"
          ]
        },
        "middleName": {
          "type": [
            "null"
          ]
        },
        "eventName": {
          "type": [
            "null"
          ]
        },
        "source": {
          "type": [
            "null"
          ]
        },
        "linkedInUrl": {
          "type": [
            "null",
            "string"
          ]
        },
        "replyCount": {
          "type": [
            "null",
            "integer"
          ]
        },
        "optedOutAt": {
          "type": [
            "null",
            "string"
          ]
        },
        "optedOut": {
          "type": [
            "null",
            "boolean"
          ]
        },
        "emails": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "school": {
          "type": [
            "null",
            "string"
          ]
        },
        "name": {
          "type": [
            "null",
            "string"
          ]
        },
        "gender": {
          "type": [
            "null"
          ]
        },
        "specialties": {
          "type": [
            "null"
          ]
        },
        "linkedInSlug": {
          "type": [
            "null",
            "string"
          ]
        },
        "addressStreet": {
          "type": [
            "null",
            "string"
          ]
        },
        "graduationDate": {
          "type": [
            "null"
          ]
        },
        "createdAt": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom30": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom31": {
          "type": [
            "null"
          ]
        },
        "custom32": {
          "type": [
            "null"
          ]
        },
        "custom33": {
          "type": [
            "null"
          ]
        },
        "custom34": {
          "type": [
            "null"
          ]
        },
        "custom35": {
          "type": [
            "null"
          ]
        },
        "dateOfBirth": {
          "type": [
            "null"
          ]
        },
        "score": {
          "type": [
            "null"
          ]
        },
        "externalId": {
          "type": [
            "null"
          ]
        },
        "campaignName": {
          "type": [
            "null"
          ]
        },
        "twitterUsername": {
          "type": [
            "null"
          ]
        },
        "degree": {
          "type": [
            "null"
          ]
        },
        "tags": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "addressCity": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom23": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom22": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom21": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom20": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom27": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom26": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom25": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom24": {
          "type": [
            "null",
            "string"
          ]
        },
        "lastName": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom29": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom28": {
          "type": [
            "null",
            "string"
          ]
        },
        "preferredContact": {
          "type": [
            "null"
          ]
        },
        "addressStreet2": {
          "type": [
            "null",
            "string"
          ]
        },
        "facebookUrl": {
          "type": [
            "null"
          ]
        },
        "timeZone": {
          "type": [
            "null",
            "string"
          ]
        },
        "timeZoneIana": {
          "type": [
            "null",
            "string"
          ]
        },
        "engagedAt": {
          "type": [
            "null",
            "string"
          ]
        },
        "stackOverflowId": {
          "type": [
            "null"
          ]
        },
        "custom16": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom17": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom14": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom15": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom12": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom13": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom10": {
          "type": [
            "null",
            "string"
          ]
        },
        "clickCount": {
          "type": [
            "null",
            "integer"
          ]
        },
        "custom18": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom19": {
          "type": [
            "null",
            "string"
          ]
        },
        "googlePlusUrl": {
          "type": [
            "null"
          ]
        },
        "timeZoneInferred": {
          "type": [
            "null"
          ]
        },
        "custom5": {
          "type": [
            "null",
            "string"
          ]
        },
        "linkedInId": {
          "type": [
            "null"
          ]
        },
        "personalNote1": {
          "type": [
            "null"
          ]
        },
        "contactHistogram": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "integer"
              ]
            }
          }
        },
        "personalNote2": {
          "type": [
            "null"
          ]
        },
        "firstName": {
          "type": [
            "null",
            "string"
          ]
        },
        "availableAt": {
          "type": [
            "null"
          ]
        },
        "stackOverflowUrl": {
          "type": [
            "null"
          ]
        },
        "region": {
          "type": [
            "null"
          ]
        },
        "custom8": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom9": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom4": {
          "type": [
            "null",
            "string"
          ]
        },
        "quoraUrl": {
          "type": [
            "null"
          ]
        },
        "custom6": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom7": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom1": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom2": {
          "type": [
            "null",
            "string"
          ]
        },
        "custom3": {
          "type": [
            "null",
            "string"
          ]
        },
        "externalOwner": {
          "type": [
            "null"
          ]
        },
        "addressCountry": {
          "type": [
            "null",
            "string"
          ]
        },
        "touchedAt": {
          "type": [
            "null",
            "string"
          ]
        },
        "linkedInConnections": {
          "type": [
            "null"
          ]
        },
        "twitterUrl": {
          "type": [
            "null"
          ]
        },
        "custom11": {
          "type": [
            "null",
            "string"
          ]
        },
        "jobStartDate": {
          "type": [
            "null",
            "string"
          ]
        },
        "websiteUrl1": {
          "type": [
            "null",
            "string"
          ]
        },
        "websiteUrl3": {
          "type": [
            "null"
          ]
        },
        "websiteUrl2": {
          "type": [
            "null"
          ]
        },
        "openCount": {
          "type": [
            "null",
            "integer"
          ]
        },
        "nickname": {
          "type": [
            "null"
          ]
        },
        "angelListUrl": {
          "type": [
            "null"
          ]
        },
        "githubUsername": {
          "type": [
            "null"
          ]
        },
        "addressState": {
          "type": [
            "null",
            "string"
          ]
        },
        "githubUrl": {
          "type": [
            "null"
          ]
        },
        "addressZip": {
          "type": [
            "null",
            "string"
          ]
        },
        "workPhones": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "mobilePhones": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "otherPhones": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        },
        "homePhones": {
          "type": [
            "null",
            "array"
          ],
          "items": {
            "type": [
              "null",
              "string"
            ]
          }
        }
      }
    },
    "type": {
      "type": [
        "null",
        "string"
      ]
    },
    "id": {
      "type": [
        "null",
        "integer"
      ]
    },
    "links": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "self": {
          "type": [
            "null",
            "string"
          ]
        }
      }
    }
  }
}
