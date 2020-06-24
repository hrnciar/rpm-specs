# Original spec file for 0.28.0 as generated by:
#     gofed repo2spec --detect github.com/coreos/ignition --commit f7079129b8651ac51dba14c3af65692bb413c1dd  --with-extra --with-build -f
# With:
#     gofed/gofed:v1.0.1 docker image
# Modified by hand for v2.0.0-alpha

# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Not all devel deps exist in Fedora so you can't install the devel rpm 
# so we need to build without devel for now
# Generate devel rpm
%global with_devel 0
# Build project from bundled dependencies
%global with_bundled 1
# Build with debug info rpm
%global with_debug 1
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

# macros for Ignition
%global provider        github
%global provider_tld    com
%global project         coreos
%global repo            ignition
# https://github.com/coreos/ignition
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}/v2
%global commit          ee616d5fb3d21babe288877e842ea137f3e68d0d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
# define ldflags, buildflags, testflags here. The ldflags were
# taken from ./build. We will need to periodically check these
# for consistency
%global ldflags ' -X github.com/coreos/ignition/v2/internal/version.Raw=%{version} '
%global buildflags %nil
%global testflags %nil

# macros for ignition-dracut
%global dracutlibdir          %{_prefix}/lib/dracut
%global dracutprovider        github
%global dracutprovider_tld    com
%global dracutproject         coreos
%global dracutrepo            ignition-dracut
# https://github.com/coreos/ignition-dracut spec2x branch
%global dracutprovider_prefix %{dracutprovider}.%{dracutprovider_tld}/%{dracutproject}/%{dracutrepo}
%global dracutimport_path     %{dracutprovider_prefix}
%global dracutcommit          bdf0a653584eb07b3ea87078ff427473821bdc2c
%global dracutshortcommit     %(c=%{dracutcommit}; echo ${c:0:7})


Name:           ignition
Version:        2.3.0
Release:        3.git%{shortcommit}%{?dist}
Summary:        First boot installer and configuration tool
License:        ASL 2.0 and BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        https://%{dracutprovider_prefix}/archive/%{dracutcommit}/%{dracutrepo}-%{dracutshortcommit}.tar.gz

%define gopath %{_datadir}/gocode
ExcludeArch: ppc64
BuildRequires: golang >= 1.10
# add non golang BuildRequires that weren't detected
BuildRequires: libblkid-devel

# Requires for 'disks' stage
%if 0%{?fedora}
Recommends: btrfs-progs
%endif
Requires: dosfstools
Requires: gdisk
Requires: dracut
Requires: dracut-network

Obsoletes: ignition-dracut < 0.31.0-3

# Main rpm package BuildRequires
%if ! 0%{?with_bundled}
# Remaining dependencies not included in main packages (sorted)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/unit)
BuildRequires: golang(github.com/coreos/vcontext/json)
BuildRequires: golang(github.com/coreos/vcontext/path)
BuildRequires: golang(github.com/coreos/vcontext/report)
BuildRequires: golang(github.com/coreos/vcontext/tree)
BuildRequires: golang(github.com/coreos/vcontext/validate)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/rpcvmx)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/vmcheck)
BuildRequires: golang(github.com/vmware/vmw-ovflib)
BuildRequires: golang(golang.org/x/net/http/httpproxy)
%endif

# Main package Provides (generated with go-mods-to-bundled-provides.py | sort)
%if 0%{?with_bundled}
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awserr)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awsutil)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client/metadata)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/corehandlers)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/processcreds)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/csm)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/defaults)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/ec2metadata)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/endpoints)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/request)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/session)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/signer/v4)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/ini)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/s3err)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkio)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkrand)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkuri)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/shareddefaults)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/eventstream/eventstreamapi)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query/queryutil)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/rest)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/restxml)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/xml/xmlutil)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3iface)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/s3/s3manager)) = 1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts)) = 1.19.11
Provides: bundled(golang(github.com/coreos/go-semver/semver)) = 0.3.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/dbus)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/journal)) = 22.0.0
Provides: bundled(golang(github.com/coreos/go-systemd/v22/unit)) = 22.0.0
Provides: bundled(golang(github.com/coreos/vcontext/json)) = 0.0.0-20190529201340.git22b159166068
Provides: bundled(golang(github.com/coreos/vcontext/path)) = 0.0.0-20190529201340.git22b159166068
Provides: bundled(golang(github.com/coreos/vcontext/report)) = 0.0.0-20190529201340.git22b159166068
Provides: bundled(golang(github.com/coreos/vcontext/tree)) = 0.0.0-20190529201340.git22b159166068
Provides: bundled(golang(github.com/coreos/vcontext/validate)) = 0.0.0-20190529201340.git22b159166068
Provides: bundled(golang(github.com/google/renameio)) = 0.1.0
Provides: bundled(golang(github.com/google/uuid)) = 1.1.1
Provides: bundled(golang(github.com/pin/tftp)) = 2.1.0
Provides: bundled(golang(github.com/pin/tftp/netascii)) = 2.1.0
Provides: bundled(golang(github.com/stretchr/testify/assert)) = 1.3.0
Provides: bundled(golang(github.com/vincent-petithory/dataurl)) = 0.0.0-20160330182126.git9a301d65acbb
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/bdoor)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/message)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcout)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/rpcvmx)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-guestinfo/vmcheck)) = 0.0.0-20170707015358.git25eff159a728
Provides: bundled(golang(github.com/vmware/vmw-ovflib)) = 0.0.0-20170608004843.git1f217b9dc714
Provides: bundled(golang(golang.org/x/net/http/httpproxy)) = 0.0.0-20190228165749.git92fc7df08ae7
Provides: bundled(golang(golang.org/x/net/idna)) = 0.0.0-20190228165749.git92fc7df08ae7
Provides: bundled(golang(golang.org/x/sys/unix)) = 0.0.0-20191110163157.gitd32e6e3b99c4
Provides: bundled(golang(golang.org/x/text/secure/bidirule)) = 0.3.0
Provides: bundled(golang(golang.org/x/text/transform)) = 0.3.0
Provides: bundled(golang(golang.org/x/text/unicode/bidi)) = 0.3.0
Provides: bundled(golang(golang.org/x/text/unicode/norm)) = 0.3.0
%endif


%description
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, networkd units, etc.), and configuring
users. On first boot, Ignition reads its configuration from a source
of truth (remote URL, network metadata service, hypervisor bridge, etc.)
and applies the configuration.

############## devel subpackage ##############

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch
License:       ASL 2.0

# devel subpackage BuildRequires
%if 0%{?with_check} && ! 0%{?with_bundled}
# These buildrequires are only for our tests (check) (sorted)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/unit)
BuildRequires: golang(github.com/coreos/vcontext/json)
BuildRequires: golang(github.com/coreos/vcontext/path)
BuildRequires: golang(github.com/coreos/vcontext/report)
BuildRequires: golang(github.com/coreos/vcontext/tree)
BuildRequires: golang(github.com/coreos/vcontext/validate)
BuildRequires: golang(github.com/google/uuid)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/rpcvmx)
BuildRequires: golang(github.com/vmware/vmw-guestinfo/vmcheck)
BuildRequires: golang(github.com/vmware/vmw-ovflib)
BuildRequires: golang(golang.org/x/net/http/httpproxy)
%endif

# devel subpackage Requires. This is basically the source code from
# all of the libraries that ignition imports during build. (sorted)
Requires:      golang(github.com/aws/aws-sdk-go/aws)
Requires:      golang(github.com/aws/aws-sdk-go/aws/awserr)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials)
Requires:      golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
Requires:      golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
Requires:      golang(github.com/aws/aws-sdk-go/aws/session)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3)
Requires:      golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
Requires:      golang(github.com/coreos/go-semver/semver)
Requires:      golang(github.com/coreos/go-systemd/dbus)
Requires:      golang(github.com/coreos/go-systemd/unit)
Requires:      golang(github.com/coreos/vcontext/json)
Requires:      golang(github.com/coreos/vcontext/path)
Requires:      golang(github.com/coreos/vcontext/report)
Requires:      golang(github.com/coreos/vcontext/tree)
Requires:      golang(github.com/coreos/vcontext/validate)
Requires:      golang(github.com/google/uuid)
Requires:      golang(github.com/pin/tftp)
Requires:      golang(github.com/vincent-petithory/dataurl)
Requires:      golang(github.com/vmware/vmw-guestinfo/rpcvmx)
Requires:      golang(github.com/vmware/vmw-guestinfo/vmcheck)
Requires:      golang(github.com/vmware/vmw-ovflib)
Requires:      golang(golang.org/x/net/http/httpproxy)

# devel subpackage Provides (sorted)
Provides:      golang(%{import_path}/config) = %{version}-%{release}
Provides:      golang(%{import_path}/config/merge) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared/errors) = %{version}-%{release}
Provides:      golang(%{import_path}/config/shared/validations) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate/tests/pkga) = %{version}-%{release}
Provides:      golang(%{import_path}/config/translate/tests/pkgb) = %{version}-%{release}
Provides:      golang(%{import_path}/config/util) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_0) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_0/types) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental/translate) = %{version}-%{release}
Provides:      golang(%{import_path}/config/v3_1_experimental/types) = %{version}-%{release}
Provides:      golang(%{import_path}/config/validate) = %{version}-%{release}
Provides:      golang(%{import_path}/tests) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/files) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/filesystems) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/general) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/partitions) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/regression) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/security) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/negative/timeouts) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/files) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/filesystems) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/general) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/partitions) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/passwd) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/proxy) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/regression) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/security) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/systemd) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/positive/timeouts) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/register) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/registry) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/servers) = %{version}-%{release}
Provides:      golang(%{import_path}/tests/types) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

############## unit-test-devel subpackage ##############
%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
License:         ASL 2.0
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/stretchr/testify/assert)
%endif

Requires:      golang(github.com/stretchr/testify/assert)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif


############## validate subpackage ##############
%package validate

Summary:  Validation tool for Ignition configs
License:  ASL 2.0

Conflicts: ignition < 0.31.0-3

%description validate
Ignition is a utility used to manipulate systems during the initramfs.
This includes partitioning disks, formatting partitions, writing files
(regular files, systemd units, networkd units, etc.), and configuring
users. On first boot, Ignition reads its configuration from a source
of truth (remote URL, network metadata service, hypervisor bridge, etc.)
and applies the configuration.

This package contains a tool for validating Ignition configurations.

############## validate-nonlinux subpackage ##############
%package validate-nonlinux

Summary:   Validation tool for Ignition configs for macOS and Windows
License:   ASL 2.0
BuildArch: noarch

Conflicts: ignition < 0.31.0-3

%description validate-nonlinux
This package contains macOS and Windows ignition-validate binaries built
through cross-compilation. Do not install it. It is only used for
building binaries to sign by Fedora release engineering and include on the
Ignition project's Github releases page.

%prep
# setup command reference: http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
# unpack source0 and apply patches
%setup -T -b 0 -q -n %{repo}-%{commit}

# unpack source1 (dracut modules)
%setup -T -D -a 1 -q -n %{repo}-%{commit}
cd %{dracutrepo}-%{dracutcommit}
mv LICENSE ../LICENSE.dracut

%build
# Set up PWD as a proper import path for go
mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{provider_prefix}

export LDFLAGS=%{ldflags}
# Enable SELinux relabeling
export LDFLAGS+=' -X github.com/coreos/ignition/v2/internal/distro.selinuxRelabel=true '

# Modules, baby!
export GO111MODULE=on
export GOFLAGS='-mod=vendor'

echo "Building ignition..."
%gobuild -o ./ignition %{import_path}/internal

echo "Building ignition-validate..."
%gobuild -o ./ignition-validate %{import_path}/validate

echo "Building macOS ignition-validate"
export GOARCH=amd64
export GOOS=darwin
%gobuild -o ./ignition-validate-x86_64-apple-darwin %{import_path}/validate

echo "Building Windows ignition-validate"
export GOARCH=amd64
export GOOS=windows
%gobuild -o ./ignition-validate-x86_64-pc-windows-gnu.exe %{import_path}/validate

# Set this back, just in case
export GOARCH=
export GOOS=linux

%install
# ignition-dracut
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
install -d -p %{buildroot}/%{_prefix}/lib/systemd/system
pushd %{dracutrepo}-%{dracutcommit} >/dev/null
cp -r dracut/* %{buildroot}/%{dracutlibdir}/modules.d/
install -m 0644 -t %{buildroot}/%{_prefix}/lib/systemd/system/ systemd/*
popd >/dev/null

# ignition
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 ./ignition-validate %{buildroot}%{_bindir}

install -d -p %{buildroot}%{_datadir}/ignition
install -p -m 0644 ./ignition-validate-x86_64-apple-darwin %{buildroot}%{_datadir}/ignition
install -p -m 0644 ./ignition-validate-x86_64-pc-windows-gnu.exe %{buildroot}%{_datadir}/ignition

# The ignition binary is only for dracut, and is dangerous to run from
# the command line.  Install directly into the dracut module dir.
install -p -m 0755 ./ignition %{buildroot}/%{dracutlibdir}/modules.d/30ignition

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go" | grep -v "vendor") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# Since we aren't packaging up the vendor directory we need to link
# back to it somehow. Hack it up so that we can add the vendor
# directory from BUILD dir as a gopath to be searched when executing
# tests from the BUILDROOT dir.
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor

export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/config
%gotest %{import_path}/config/merge
%gotest %{import_path}/config/translate
%gotest %{import_path}/config/v3_0
%gotest %{import_path}/config/v3_0/types
%gotest %{import_path}/config/validate
%gotest %{import_path}/internal/exec/stages/files
%gotest %{import_path}/internal/exec/util
%gotest %{import_path}/internal/registry
%gotest %{import_path}/internal/util
%gotest %{import_path}/tests
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE LICENSE.dracut
%doc README.md doc/
%{dracutlibdir}/modules.d/*
%{_prefix}/lib/systemd/system/*.service

%files validate
%doc README.md
%license LICENSE
%{_bindir}/%{name}-validate

%files validate-nonlinux
%license LICENSE
%dir %{_datadir}/ignition
%{_datadir}/ignition/ignition-validate-x86_64-apple-darwin
%{_datadir}/ignition/ignition-validate-x86_64-pc-windows-gnu.exe

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%endif

%changelog
* Mon Jun 15 2020 Timothée Ravier <travier@redhat.com> - 2.3.0-3.gitee616d5
- Update to latest ignition-dracut to fix coreos-gpt-setup unit
  https://github.com/coreos/ignition-dracut/pull/191

* Mon Jun 01 2020 Jonathan Lebon <jonathan@jlebon.com> - 2.3.0-2.gitee616d5
- Update to latest ignition-dracut to fix error handling
  https://github.com/coreos/ignition-dracut/pull/188

* Tue May 05 2020 Benjamin Gilbert <bgilbert@redhat.com> - 2.3.0-1.gitee616d5
- New release
- Bump ignition-dracut

* Sun Apr 26 2020 Dusty Mabe <dusty@dustymabe.com> - 2.2.1-5.git2d3ff58
- Update to latest ignition-dracut for network fixes
  https://github.com/coreos/ignition-dracut/pull/174

* Thu Apr 16 2020 Colin Walters <walters@verbum.org> - 2.2.1-4.git2d3ff58
- Update to latest ignition-dracut for virtio dump

* Mon Mar 30 2020 Benjamin Gilbert <bgilbert@redhat.com> - 2.2.1-3.git2d3ff58
- Bump ignition-dracut to fix umount stage network access

* Sat Mar 28 2020 Benjamin Gilbert <bgilbert@redhat.com> - 2.2.1-2.git2d3ff58
- Fix userdata/metadata fetch on Packet

* Tue Mar 24 2020 Benjamin Gilbert <bgilbert@redhat.com> - 2.2.1-1.git2d3ff58
- New release
- Bump ignition-dracut for initramfs network teardown

* Sat Feb 01 2020 Benjamin Gilbert <bgilbert@redhat.com> - 2.1.1-6.git40c0b57
- Switch -validate-nonlinux to noarch; move files to /usr/share/ignition
- Improve -validate-nonlinux descriptive text

* Fri Jan 31 2020 Jonathan Lebon <jonathan@jlebon.com> - 2.1.1-5.git40c0b57
- Bump ignition-dracut for ignition-diskful-subsequent target
  https://github.com/coreos/ignition-dracut/pull/151
- Kill grub dropin
  https://github.com/coreos/ignition-dracut/pull/91

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4.git40c0b57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Dusty Mabe <dusty@dustymabe.com> - 2.1.1-3.git40c0b57
- Backport upstream patch to workaround problem booting on live systems
    - https://github.com/coreos/fedora-coreos-tracker/issues/339
    - https://github.com/coreos/ignition/pull/907

* Tue Dec 17 2019 Andrew Jeddeloh <ajeddelo@redhat.com> - 2.1.1-2.git40c0b57
- Add ignition-validate-nonlinux subpackage. This should not be installed. It
  is only used for building binaries to sign by Fedora release engineering and
  include on the Ignition project's Github releases page.

* Fri Dec 13 2019 Andrew Jeddeloh <ajeddelo@redhat.com> - 2.1.1-1.git40c0b57
- New release 2.1.1

* Mon Dec 09 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.1-9.gita8f91fa
- Use the master branch of ignition-dracut, not spec2x

* Fri Dec 06 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.1-8.gita8f91fa
- Bump Ignition for that sweet SELinux labeling:
  https://github.com/coreos/ignition/pull/846

* Thu Dec 05 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.1-7.git641ec6a
- Don't require btrfs-progs, just recommend it
  https://github.com/coreos/fedora-coreos-tracker/issues/323

* Wed Dec 04 2019 Allen Bai <abai@redhat.com> - 2.0.1-6.git641ec6a
- Update dracut to latest spec2x
    * firstboot-complete: tell zipl to run

* Thu Oct 31 2019 Colin Walters <walters@verbum.org> - 2.0.1-5.git641ec6a
- Update dracut

* Wed Sep 25 2019 Colin Walters <walters@verbum.org> - 2.0.1-4.git641ec6a
- Bump to latest in prep for rootfs redeploy work

* Sat Sep 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-3.gite75cf24
- Fix up arch dependencies for new golang specs

* Fri Aug 16 2019 Colin Walters <walters@verbum.org> - 2.0.1-2.gite75cf24
- Update dracut for gpt fixes

* Thu Jul 25 2019 Andrew Jeddeloh <ajeddelo@redhat.com> - 2.0.1-1.gite75cf24
- New release 2.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.git0c1da80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Andrew Jeddeloh <ajeddelo@redhat.com> - 2.0.0-1.git0c1da80
- New release 2.0.0

* Fri May 03 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.0-beta.3.git910e6c6
- Adapt distro.selinuxRelabel flag path for v2/ move

* Fri May 03 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.0-beta.2.git910e6c6
- Bump ignition-dracut dropping CoreOS integration files

* Mon Apr 29 2019 Andrew Jeddeloh <ajeddelo@redhat.com> - 2.0.0-beta.1.git910e6c6
- New release 2.0.0-beta

* Mon Apr 08 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.0-alpha.3.git906cf04
- ignition-dracut: update to latest
    * dracut/30ignition: link to RHBZ in ignition-complete
    * dracut/30ignition: add OnFailure= for ExecStop= services
    * dracut/30ignition: order ExecStop= units before initrd-switch-root.target
    * dracut/30ignition: re-order directives in remount-sysroot
    * dracut/30ignition: add missing Before= for mount unit
    * dracut/30ignition: order ignition-complete.target before initrd.target
    * module_setup: include cdrom rules for openstack

* Wed Mar 27 2019 Benjamin Gilbert <bgilbert@backtick.net> - 2.0.0-alpha.2.git906cf04
- Backport fix for SELinux relabeling of systemd units
- Drop obsolete override of chroot path

* Wed Mar 27 2019 Jonathan Lebon <jonathan@jlebon.com> - 2.0.0-alpha.1.git906cf04
- New release 2.0.0-alpha
- ignition-dracut: Go back to master branch

* Fri Mar 22 2019 Dusty Mabe <dusty@dustymabe.com> - 0.31.0-7.gitf59a653
- ignition-dracut: Pull in latest from spec2x branch
    * grub: support overriding network kcmdline args
- ignition: pull in subuid/subgid files patch from spec2x branch
    * stages/files: Also relabel subuid/subgid files

* Wed Mar 20 2019 Michael Nguyen <mnguyen@redhat.com> - 0.31.0-6.gitf59a653
- Backport patch for supporting guestinfo.ignition.config.data

* Mon Mar 18 2019 Dusty Mabe <dusty@dustymabe.com> - 0.31.0-5.gitf59a653
- Use the spec2x branch of ignition-dracut upstream
- * Since ignition-dracut master has moved to supporting ignition
    spec 3.x we are applying 2.x related fixes to the spec2x
    branch in the ignition-dracut repo.
  * Summary of backports: https://github.com/coreos/ignition-dracut/pull/58

* Mon Mar 18 2019 Benjamin Gilbert <bgilbert@backtick.net> - 0.31.0-4.gitf59a653
- Move dracut modules into main ignition package
- Move ignition binary out of the PATH
- Move ignition-validate into a subpackage
- Include ignition-dracut license file
- Drop developer docs from base package

* Mon Mar 18 2019 Colin Walters <walters@verbum.org> - 0.31.0-3.gitf59a653
- Backport patch for networking

* Mon Mar 04 2019 Dusty Mabe <dusty@dustymabe.com> - 0.31.0-2.gitf59a653
- ignition-dracut: backport patch for finding ignition.firstboot file on UEFI systems
  https://github.com/coreos/ignition-dracut/pull/52

* Wed Feb 20 2019 Andrew Jeddeloh <andrew.jeddeloh@redhat.com> - 0.31.0-1.gitf59a653
- New release 0.31.0

* Fri Feb 15 2019 Dusty Mabe <dusty@dustymabe.com> - 0.30.0-4.git308d7a0
- Bump to ignition-dracut 2c69925
- * support platform configs and user configs in /boot
    ^ https://github.com/coreos/ignition-dracut/pull/43
  * Add ability to parse config.ign file on boot
    ^ https://github.com/coreos/ignition-dracut/pull/42

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3.git308d7a0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Dusty Mabe <dusty@dustymabe.com> - 0.30.0-2.git308d7a0
- Bump to ignition-dracut fa7131b
- * 7579b92 journal: add clarifying comment for context
  * a6551f1 Remount /sysroot rw (#38)
  * ignition-firstboot-complete.service: Remount /boot rw

* Sat Dec 15 2018 Benjamin Gilbert <bgilbert@redhat.com> - 0.30.0-1.git308d7a0
- New release 0.30.0

* Fri Dec 14 2018 Michael Nguyen <mnguyen@redhat.com> - 0.29.1-3.gitb1ab0b2
- define gopath for RHEL7

* Tue Dec 11 2018 Dusty Mabe <dusty@dustymabe.com> - 0.29.1-2.gitb1ab0b2
- require golang >= 1.10 and specify architecture list for RHEL7

* Tue Dec 11 2018 Andrew Jeddeloh <andrew.jeddeloh@redhat.com> - 0.29.1-1.gitb1ab0b2
- New release 0.29.1

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.0-12.gitf707912
- Rebuild for protobuf 3.6 in rawhide (f30)

* Tue Nov 20 2018 Jonathan Lebon <jonathan@jlebon.com> - 0.28.0-11.git7b83454
- Bump to ignition-dracut 7b83454

* Thu Oct 25 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-10.gitf707912
- Bump to ignition-dracut decf63f
- * 03d8438 30ignition: only instmods if module available
  
* Thu Oct 25 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-9.gitf707912
- Bump to ignition-dracut 7ee64ca
- * 3ec0b39 remove ignition-remount-sysroot.service files
  * 66335f2 ignition: run files stage at original CL ordering
  * 0301a03 ignition-disks.service: drop Requires=network.target
  * a0bc135 ignition-ask-var-mount.service: use RemainAfterExit=yes
  * ecf5779 module-setup.sh: explicitly install qemu_fw_cfg

* Mon Oct 15 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-8.gitf707912
- Bump to ignition-dracut 4bdfb34
- * 6d0763a module-setup: Make mkfs.btrfs optional

* Wed Oct 10 2018 Jonathan Lebon <jonathan@jlebon.com> - 0.28.0-7.gitf707912
- Backport patch for handling sysctl files correctly
  https://github.com/coreos/coreos-assembler/pull/128
  https://github.com/openshift/machine-config-operator/pull/123

* Wed Sep 26 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-6.gitf707912
- Bump to ignition-dracut c09ce6f
- * ce9f648 30ignition: add support for ignition-disks

* Mon Sep 24 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-5.gitf707912
- Remove requires for btrfs on !fedora
- Bump to ignition-dracut 8c85eb3
- * 26f2396 journal: Don't log to console AND kmsg

* Mon Sep 17 2018 Jonathan Lebon <jonathan@jlebon.com> - 0.28.0-4.gitf707912
- Backport patch for relabeling /var/home on FCOS
  https://github.com/coreos/fedora-coreos-config/issues/2

* Thu Sep 06 2018 Luca Bruno <lucab@fedoraproject.org> - 0.28.0-3.gitf707912
- Add requires for disks stage

* Thu Aug 30 2018 Dusty Mabe <dusty@dustymabe.com> - 0.28.0-2.gitf707912
- Bump to ignition-dracut d056287
- * 3f41219 dracut/ignition: remove CL-legacy udev references
- * 92ef9dd coreos-firstboot-complete: RemainAfterExit=yes

* Thu Aug 30 2018 Andrew Jeddeloh <andrewjeddeloh@redhat.com> - 0.28.0-1.gitf707912
- New release 0.28.0

* Fri Aug 17 2018 Dusty Mabe <dusty@dustymabe.com> - 0.27.0-3.gitcc7ebe0
- Bump to ignition-dracut 56aa514

* Wed Aug 15 2018 Jonathan Lebon <jonathan@jlebon.com> - 0.27.0-2.gitcc7ebe0
- Backport patch for /root relabeling
  https://github.com/coreos/ignition/pull/613

* Fri Aug 10 2018 Jonathan Lebon <jonathan@jlebon.com> - 0.27.0-1.gitcc7ebe0
- New release 0.27.0

* Sat Jul 21 2018 Dusty Mabe <dusty@dustymabe.com> - 0.26.0-0.6.git7610725
- Bump to ignition-dracut d664657

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-0.5.git7610725
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Dusty Mabe <dusty@dustymabe.com> - 0.26.0-0.4.git7610725
- Fix building on el7 (install -D not working)

* Fri Jun 29 2018 Dusty Mabe <dusty@dustymabe.com> - 0.26.0-0.3.git7610725
- Bump to ignition-dracut 17a201b

* Tue Jun 26 2018 Dusty Mabe <dusty@dustymabe.com> - 0.26.0-0.2.git7610725
- Rename dustymabe/bootengine upstrem to dustymabe/ignition-dracut

* Thu Jun 21 2018 Dusty Mabe <dusty@dustymabe.com> - 0.26.0-0.1.git7610725
- First package for Fedora

