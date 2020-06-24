%if (0%{?fedora} && 0%{?fedora >= 31})
    %define have_go_rpm_macros 1
%else
    %define have_go_rpm_macros 0
%endif

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if ! 0%{?gobuild:1}
# %gobuild not available on RHEL. Definition lifted from Fedora33 podman.spec and tested on RHEL-8.2
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v -x %{?**};
%endif

%global domain          github.com
%global org             kata-containers
%global repo            proxy
%global download        %{domain}/%{org}/%{repo}
%global importname      %{download}

# Release candidate version tracking
# global rcver rc0
%if 0%{?rcver:1}
%global rcrel .%{rcver}
%global rcstr -%{rcver}
%endif

Name:      kata-%{repo}
Version:   1.11.0
Release:   1%{?rcrel}%{?dist}
Url:       https://%{download}
Source0:   https://%{download}/archive/%{version}%{?rcstr}/%{repo}-%{version}%{?rcstr}.tar.gz

Summary:   Proxy for Kata Containers
Group:     Development/Tools
License:   ASL 2.0

%if 0%{?have_go_rpm_macros}
BuildRequires: go-rpm-macros
%else
BuildRequires: compiler(go-compiler)
BuildRequires: golang
%endif

Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.0
Provides: bundled(golang(github.com/hashicorp/yamux)) = f5742cb6
Provides: bundled(golang(github.com/pmezard/go-difflib)) = v1.0.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.0.4
Provides: bundled(golang(github.com/stretchr/testify)) = v1.2.1
Provides: bundled(golang(golang.org/x/crypto)) = 13931e22f9e72ea58bb73048bc752b48c6d4d4ac
Provides: bundled(golang(golang.org/x/sys)) = 810d7000345868fc619eb81f46307107118f4ae1

%description
A proxy for the Kata Containers project

The Kata Containers runtime creates a virtual machine (VM) to isolate
a set of container workloads. The VM requires a guest kernel and a
guest operating system ("guest OS") to boot and create containers
inside the guest environment. This package contains the tools to create
guest OS images.

The kata-proxy is part of the Kata Containers project. For more
information on how the proxy fits into the Kata Containers
architecture, refer to the Kata Containers architecture documentation.

%prep
%autosetup -n %{repo}-%{version}%{?rcstr}

%build
# Adjust for go build requirements
# Future: Use %%gopkginstall
# export GOROOT="$(pwd)/go"
export GOPATH="$(pwd)/go"

mkdir go
mv vendor go/src
mkdir -p go/src/%{domain}/%{org}
ln -s $(pwd)/../%{repo}-%{version}%{?rcstr} go/src/%{importname}
cd go/src/%{importname}

LDFLAGS="-linkmode=external"
%gobuild

%install
# install binaries
install -dp %{buildroot}%{_libexecdir}/kata-containers
install -p -m 755 proxy %{buildroot}%{_libexecdir}/kata-containers/%{name}

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%dir %{_libexecdir}/kata-containers
%{_libexecdir}/kata-containers/%{name}

%changelog
* Fri May 08 2020 Cole Robinson <crobinso@redhat.com> - 1.11.0-1
- Update to version 1.11.0

* Mon Apr 20 2020 Cole Robinson <aintdiscole@gmail.com> - 1.11.0-0.1.rc0
- Update to 1.11.0-rc0

* Mon Mar 23 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.11.0-0.alpha1
- Update to release 1.11.0-alpha1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.10.0-1
- Update to release 1.10.0
  + Overwrite PREFIX
  + Use xenial

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.3-1
- Update to release 1.9.3 (no changes upstream)

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.2-1
- Update to release 1.9.2 (no changes upstream)

* Fri Nov 29 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.1-1
- Update to release 1.9.1

* Fri Nov 29 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.0-2
- Address rpmlint warning about macro in comment

* Thu Nov 14 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.0-1
- Update to release 1.9.0

* Fri Sep 20 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.8.2-1
- Update to 1.8.2 release

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-5.gitd364b2e
- build for all arches

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-4.gitd364b2e
- no need to specify systemd as BR

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-3.gitd364b2e
- no need to specify make as BR

* Mon Nov 12 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-2.gitd364b2e
- bundled Provides

* Sat Nov 10 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-1.gitd364b2e
- bump to v1.3.1
- built commit d364b2e

* Thu Jun 14 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.gita69326b
- first build (ready for Fedora review)
