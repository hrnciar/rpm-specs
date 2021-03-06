# Do not build with tests by default
# Pass --with tests to rpmbuild to override
%bcond_with tests

%global goipath         github.com/osbuild/osbuild-composer

Version:        22

%gometa

%global common_description %{expand:
An image building service based on osbuild
It is inspired by lorax-composer and exposes the same API.
As such, it is a drop-in replacement.
}

Name:           osbuild-composer
Release:        1%{?dist}
Summary:        An image building service based on osbuild

# osbuild-composer doesn't have support for building i686 images
# and also RHEL and Fedora has now only limited support for this arch.
ExcludeArch:    i686

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}


BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  systemd
BuildRequires:  krb5-devel
%if 0%{?fedora}
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  golang(github.com/aws/aws-sdk-go)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/deepmap/oapi-codegen/pkg/codegen)
BuildRequires:  golang(github.com/go-chi/chi)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/julienschmidt/httprouter)
BuildRequires:  golang(github.com/kolo/xmlrpc)
BuildRequires:  golang(github.com/labstack/echo/v4)
BuildRequires:  golang(github.com/gobwas/glob)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/gophercloud/gophercloud)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/ubccr/kerby)
BuildRequires:  golang(github.com/vmware/govmomi)
%endif

Requires: %{name}-worker = %{version}-%{release}
Requires: systemd
Requires: osbuild >= 18
Requires: osbuild-ostree >= 18
Requires: qemu-img

Provides: weldr

%if 0%{?rhel}
Obsoletes: lorax-composer <= 29
Conflicts: lorax-composer
%endif

# Remove when we stop releasing into Fedora 35
%if 0%{?fedora} >= 34
# lorax 34.3 is the first one without the composer subpackage
Obsoletes: lorax-composer < 34.3
%endif

# remove in F34
Obsoletes: golang-github-osbuild-composer < %{version}-%{release}
Provides:  golang-github-osbuild-composer = %{version}-%{release}

%description
%{common_description}

%prep
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep
%endif

%if 0%{?fedora} && 0%{?fedora} <= 32
# Fedora 32 and older ships a different kolo/xmlrpc API. We cannot specify
# build tags in gobuild macro because the macro itself specifies build tags.
# and -tags argument cannot be used more than once.
# Therefore, this ugly hack with build tags switcharoo is required.
# Remove when F32 is EOL.

# Remove the build constraint from the wrapper of the old API
sed -i "s$// +build kolo_xmlrpc_oldapi$// +build !kolo_xmlrpc_oldapi$" internal/upload/koji/xmlrpc-response-oldapi.go

# Add a build constraint to the wrapper of the new API
sed -i "s$// +build !kolo_xmlrpc_oldapi$// +build kolo_xmlrpc_oldapi$" internal/upload/koji/xmlrpc-response.go
%endif

%build
%if 0%{?rhel}
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
export GOFLAGS=-mod=vendor
%endif

%gobuild -o _bin/osbuild-composer %{goipath}/cmd/osbuild-composer
%gobuild -o _bin/osbuild-worker %{goipath}/cmd/osbuild-worker


%if %{with tests} || 0%{?rhel}

# Build test binaries with `go test -c`, so that they can take advantage of
# golang's testing package. The golang rpm macros don't support building them
# directly. Thus, do it manually, taking care to also include a build id.
#
# On Fedora, also turn off go modules and set the path to the one into which
# the golang-* packages install source code.
%if 0%{?fedora}
export GO111MODULE=off
export GOPATH=%{gobuilddir}:%{gopath}
%endif

TEST_LDFLAGS="${LDFLAGS:-} -B 0x$(od -N 20 -An -tx1 -w100 /dev/urandom | tr -d ' ')"

go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-composer-cli-tests %{goipath}/cmd/osbuild-composer-cli-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-dnf-json-tests %{goipath}/cmd/osbuild-dnf-json-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-weldr-tests %{goipath}/internal/client/
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-image-tests %{goipath}/cmd/osbuild-image-tests
go test -c -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/osbuild-auth-tests %{goipath}/cmd/osbuild-auth-tests
go build -tags=integration -ldflags="${TEST_LDFLAGS}" -o _bin/cloud-cleaner %{goipath}/cmd/cloud-cleaner

%endif

%install
install -m 0755 -vd                                             %{buildroot}%{_libexecdir}/osbuild-composer
install -m 0755 -vp _bin/osbuild-composer                       %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp _bin/osbuild-worker                         %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp dnf-json                                    %{buildroot}%{_libexecdir}/osbuild-composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/osbuild-composer/repositories
install -m 0644 -vp repositories/*                              %{buildroot}%{_datadir}/osbuild-composer/repositories/

install -m 0755 -vd                                             %{buildroot}%{_unitdir}
install -m 0644 -vp distribution/osbuild-composer.service       %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-composer.socket        %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-remote-worker.socket   %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-remote-worker@.service %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-worker@.service        %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-composer-api.socket    %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-composer-koji.socket   %{buildroot}%{_unitdir}/
install -m 0755 -vd                                             %{buildroot}%{_unitdir}
install -m 0644 -vp distribution/osbuild-composer.{service,socket} %{buildroot}%{_unitdir}/
install -m 0644 -vp distribution/osbuild-*worker*.{service,socket} %{buildroot}%{_unitdir}/

install -m 0755 -vd                                             %{buildroot}%{_sysusersdir}
install -m 0644 -vp distribution/osbuild-composer.conf          %{buildroot}%{_sysusersdir}/

install -m 0755 -vd                                             %{buildroot}%{_localstatedir}/cache/osbuild-composer/dnf-cache

%if %{with tests} || 0%{?rhel}

install -m 0755 -vd                                             %{buildroot}%{_libexecdir}/tests/osbuild-composer
install -m 0755 -vp _bin/osbuild-composer-cli-tests             %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp _bin/osbuild-weldr-tests                    %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp _bin/osbuild-dnf-json-tests                 %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp _bin/osbuild-image-tests                    %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp _bin/osbuild-auth-tests                     %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp test/cmd/*                                  %{buildroot}%{_libexecdir}/tests/osbuild-composer/
install -m 0755 -vp _bin/cloud-cleaner                          %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp tools/image-info                            %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp tools/run-koji-container.sh                 %{buildroot}%{_libexecdir}/osbuild-composer/
install -m 0755 -vp tools/koji-compose.py                       %{buildroot}%{_libexecdir}/osbuild-composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/ansible
install -m 0644 -vp test/data/ansible/*                         %{buildroot}%{_datadir}/tests/osbuild-composer/ansible/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/azure
install -m 0644 -vp test/data/azure/*                           %{buildroot}%{_datadir}/tests/osbuild-composer/azure/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/ca
install -m 0755 -vp test/data/ca/ca-crt.pem                     %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0600 -vp test/data/ca/ca-key.pem                     %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0755 -vp test/data/ca/composer-crt.pem               %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0600 -vp test/data/ca/composer-key.pem               %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0755 -vp test/data/ca/worker-crt.pem                 %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0600 -vp test/data/ca/worker-key.pem                 %{buildroot}%{_datadir}/tests/osbuild-composer/ca/

# Client keys are used by tests to access the composer APIs. Allow all users access.
install -m 0755 -vp test/data/ca/client-crt.pem                 %{buildroot}%{_datadir}/tests/osbuild-composer/ca/
install -m 0755 -vp test/data/ca/client-key.pem                 %{buildroot}%{_datadir}/tests/osbuild-composer/ca/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/cases
install -m 0644 -vp test/data/cases/*                           %{buildroot}%{_datadir}/tests/osbuild-composer/cases/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init
install -m 0644 -vp test/data/cloud-init/*                      %{buildroot}%{_datadir}/tests/osbuild-composer/cloud-init/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/composer
install -m 0644 -vp test/data/composer/*                        %{buildroot}%{_datadir}/tests/osbuild-composer/composer/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos
install -m 0644 -vp test/data/kerberos/*                        %{buildroot}%{_datadir}/tests/osbuild-composer/kerberos/

install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/keyring
install -m 0644 -vp test/data/keyring/id_rsa.pub                %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/
install -m 0600 -vp test/data/keyring/id_rsa                    %{buildroot}%{_datadir}/tests/osbuild-composer/keyring/

%if 0%{?rhel}
install -m 0755 -vd                                             %{buildroot}%{_datadir}/tests/osbuild-composer/vendor
install -m 0644 -vp test/data/vendor/87-podman-bridge.conflist  %{buildroot}%{_datadir}/tests/osbuild-composer/vendor/
install -m 0755 -vp test/data/vendor/dnsname                    %{buildroot}%{_datadir}/tests/osbuild-composer/vendor/
%endif

%endif

%check
%if 0%{?rhel}
export GOFLAGS=-mod=vendor
export GOPATH=$PWD/_build:%{gopath}
# cd inside GOPATH, otherwise go with GO111MODULE=off ignores vendor directory
cd $PWD/_build/src/%{goipath}
%gotest ./...
%else
%gocheck
%endif

%post
%systemd_post osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%preun
%systemd_preun osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%postun
%systemd_postun_with_restart osbuild-composer.service osbuild-composer.socket osbuild-composer-api.socket osbuild-remote-worker.socket

%files
%license LICENSE
%doc README.md
%{_libexecdir}/osbuild-composer/osbuild-composer
%{_libexecdir}/osbuild-composer/dnf-json
%{_datadir}/osbuild-composer/
%{_unitdir}/osbuild-composer.service
%{_unitdir}/osbuild-composer.socket
%{_unitdir}/osbuild-composer-api.socket
%{_unitdir}/osbuild-remote-worker.socket
%{_sysusersdir}/osbuild-composer.conf

%package worker
Summary:    The worker for osbuild-composer
Requires:   systemd
Requires:   osbuild

# remove in F34
Obsoletes: golang-github-osbuild-composer-worker < %{version}-%{release}
Provides:  golang-github-osbuild-composer-worker = %{version}-%{release}

%description worker
The worker for osbuild-composer

%files worker
%{_libexecdir}/osbuild-composer/osbuild-worker
%{_unitdir}/osbuild-worker@.service
%{_unitdir}/osbuild-remote-worker@.service

%post worker
%systemd_post osbuild-worker@.service osbuild-remote-worker@.service

%preun worker
# systemd_preun uses systemctl disable --now which doesn't work well with template services.
# See https://github.com/systemd/systemd/issues/15620
# The following lines mimicks its behaviour by running two commands:

# disable and stop all the worker services
systemctl --no-reload disable osbuild-worker@.service osbuild-remote-worker@.service
systemctl stop "osbuild-worker@*.service" "osbuild-remote-worker@*.service"

%postun worker
# restart all the worker services
%systemd_postun_with_restart "osbuild-worker@*.service" "osbuild-remote-worker@*.service"

%if %{with tests} || 0%{?rhel}

%package tests
Summary:    Integration tests
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-koji = %{version}-%{release}
Requires:   composer-cli
Requires:   createrepo_c
Requires:   genisoimage
Requires:   qemu-kvm-core
Requires:   systemd-container
Requires:   jq
Requires:   unzip
Requires:   container-selinux
Requires:   dnsmasq
Requires:   krb5-workstation
Requires:   koji
Requires:   podman
Requires:   python3
Requires:   sssd-krb5
Requires:   libvirt-client libvirt-daemon
Requires:   libvirt-daemon-config-network
Requires:   libvirt-daemon-config-nwfilter
Requires:   libvirt-daemon-driver-interface
Requires:   libvirt-daemon-driver-network
Requires:   libvirt-daemon-driver-nodedev
Requires:   libvirt-daemon-driver-nwfilter
Requires:   libvirt-daemon-driver-qemu
Requires:   libvirt-daemon-driver-secret
Requires:   libvirt-daemon-driver-storage
Requires:   libvirt-daemon-driver-storage-disk
Requires:   libvirt-daemon-kvm
Requires:   qemu-img
Requires:   qemu-kvm
Requires:   virt-install
Requires:   expect
Requires:   python3-lxml
Requires:   ansible
Requires:   httpd
%if 0%{?fedora}
Requires:   podman-plugins
%endif
%ifarch %{arm}
Requires:   edk2-aarch64
%endif

%description tests
Integration tests to be run on a pristine-dedicated system to test the osbuild-composer package.

%files tests
%{_libexecdir}/tests/osbuild-composer/
%{_datadir}/tests/osbuild-composer/
%{_libexecdir}/osbuild-composer/cloud-cleaner
%{_libexecdir}/osbuild-composer/image-info
%{_libexecdir}/osbuild-composer/run-koji-container.sh
%{_libexecdir}/osbuild-composer/koji-compose.py

%endif

%package koji
Summary:    osbuild-composer for pushing images to Koji
Requires:   %{name} = %{version}-%{release}

# remove in F34
Obsoletes: golang-github-osbuild-composer-rcm < %{version}-%{release}
Provides:  golang-github-osbuild-composer-rcm = %{version}-%{release}
# remove in the future
Obsoletes: osbuild-composer-rcm < %{version}-%{release}
Provides:  osbuild-composer-rcm = %{version}-%{release}

%description koji
osbuild-composer specifically for pushing images to Koji. This package is only
needed for backwards compatibility and will be removed in the future.

%files koji
%{_unitdir}/osbuild-composer-koji.socket

%post koji
%systemd_post osbuild-composer-koji.socket

%preun koji
%systemd_preun osbuild-composer-koji.socket

%postun koji
%systemd_postun_with_restart osbuild-composer-koji.socket

%changelog
* Fri Oct 16 2020 Ondrej Budai <obudai@redhat.com> - 22-1
- New upstream release

* Sun Aug 23 2020 Tom Gundersen <teg@jklm.no> - 20-1
- New upstream release

* Tue Aug 11 2020 Tom Gundersen <teg@jklm.no> - 19-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Ondrej Budai <obudai@redhat.com> - 18-1
- New upstream release

* Wed Jul 08 2020 Ondrej Budai <obudai@redhat.com> - 17-1
- New upstream release

* Mon Jun 29 2020 Ondrej Budai <obudai@redhat.com> - 16-1
- New upstream release

* Fri Jun 12 2020 Ondrej Budai <obudai@redhat.com> - 15-1
- New upstream release

* Thu Jun 04 2020 Ondrej Budai <obudai@redhat.com> - 14-1
- New upstream release

* Fri May 29 2020 Ondrej Budai <obudai@redhat.com> - 13-2
- Add missing osbuild-ostree dependency

* Thu May 28 2020 Ondrej Budai <obudai@redhat.com> - 13-1
- New upstream release

* Thu May 14 2020 Ondrej Budai <obudai@redhat.com> - 12-1
- New upstream release

* Wed Apr 29 2020 Ondrej Budai <obudai@redhat.com> - 11-1
- New upstream release

* Wed Apr 15 2020 Ondrej Budai <obudai@redhat.com> - 10-1
- New upstream release

* Wed Apr 01 2020 Ondrej Budai <obudai@redhat.com> - 9-1
- New upstream release

* Mon Mar 23 2020 Ondrej Budai <obudai@redhat.com> - 8-1
- Initial package (renamed from golang-github-osbuild-composer)
