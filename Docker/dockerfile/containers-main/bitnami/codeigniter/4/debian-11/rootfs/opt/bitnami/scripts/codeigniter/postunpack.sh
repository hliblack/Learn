#!/bin/bash
# Copyright VMware, Inc.
# SPDX-License-Identifier: APACHE-2.0

# shellcheck disable=SC1091

set -o errexit
set -o nounset
set -o pipefail
# set -o xtrace # Uncomment this line for debugging purposes

# Load libraries
. /opt/bitnami/scripts/libcodeigniter.sh
. /opt/bitnami/scripts/libfs.sh
. /opt/bitnami/scripts/libos.sh

# Load CodeIgniter environment
. /opt/bitnami/scripts/codeigniter-env.sh

# Ensure required directories exist
ensure_dir_exists "/app"
configure_permissions_ownership "/app" -d "775" -f "664"