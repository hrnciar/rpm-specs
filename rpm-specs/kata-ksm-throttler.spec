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
%global repo            ksm-throttler
%global download        %{domain}/%{org}/%{repo}
%global importname      %{download}

# Release candidate version tracking
# global rcver rc0
%if 0%{?rcver:1}
%global rcrel .%{rcver}
%global rcstr -%{rcver}
%endif


Name:      kata-%{repo}
Version:   1.11.1
Release:   1%{?rcrel}%{?dist}.1
Url:       https://%{download}
Source0:   https://%{download}/archive/%{version}%{?rcstr}/%{repo}-%{version}%{?rcstr}.tar.gz
Summary:   Kata KSM throttling daemon
Group:     Development/Tools
License:   ASL 2.0

%if 0%{?have_go_rpm_macros}
BuildRequires: go-rpm-macros
%else
BuildRequires: compiler(go-compiler)
BuildRequires: golang
%endif
BuildRequires: systemd

Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.0
Provides: bundled(golang(github.com/fsnotify/fsnotify)) = 4da3e2cfbabc9f751898f250b49f2439785783a1
Provides: bundled(golang(github.com/golang/protobuf)) = 1e59b77b52bf8e4b449a57e6f79f21226d571845
Provides: bundled(golang(github.com/pmezard/go-difflib)) = v1.0.0
Provides: bundled(golang(github.com/sirupsen/logrus)) = v1.0.3
Provides: bundled(golang(github.com/stretchr/testify)) = 2aa2c176b9dab406a6970f6a55f513e8a8c8b18f
Provides: bundled(golang(golang.org/x/crypto)) = 9f005a07e0d31d45e6656d241bb5c0f2efd4bc94
Provides: bundled(golang(golang.org/x/net)) = a337091b0525af65de94df2eb7e98bd9962dcbe2
Provides: bundled(golang(golang.org/x/sys)) = bf42f188b9bc6f2cf5b8ee5a912ef1aedd0eba4c
Provides: bundled(golang(golang.org/x/text)) = 88f656faf3f37f690df1a32515b479415e1a6769
Provides: bundled(golang(google.golang.org/genproto)) = 11c7f9e547da6db876260ce49ea7536985904c9b
Provides: bundled(golang(google.golang.org/grpc)) = v1.7.3

%description
This project implements a Kernel Same-page Merging throttling daemon.

The Kata Containers runtime creates a virtual machine (VM) to isolate
a set of container workloads. The VM requires a guest kernel and a
guest operating system ("guest OS") to boot and create containers
inside the guest environment. This package contains the tools to create
guest OS images.

The goal of the ksm throttler daemon is to regulate KSM by dynamically
modifying the KSM sysfs entries, in order to minimize memory
duplication as fast as possible while keeping the KSM daemon load low.

%prep
%autosetup -n %{repo}-%{version}%{?rcstr}
for file in kata-%{repo}.service.in kata-vc-throttler.service.in
do
    sed -i "s|@libexecdir@|%{_libexecdir}|g" $file
    sed -i "s|@PACKAGE_NAME@|%{repo}|g" $file
    sed -i "s|@TARGET@|%{repo}|g" $file
    sed -i "s|@PACKAGE_URL@|%{download}|g" $file
    sed -i "s|@SERVICE_FILE@|%{name}.service|g" $file
done

%build
# Adjust for go build requirements
# Future: Use %gopkginstall
# export GOROOT="$(pwd)/go"
export GOPATH="$(pwd)/go"

mkdir go
mv vendor go/src
mkdir -p go/src/%{domain}/%{org}
ln -s $(pwd)/../%{repo}-%{version}%{?rcstr} go/src/%{importname}
cd go/src/%{importname}

LDFLAGS="-linkmode=external"
%gobuild

pushd trigger/kicker
%gobuild
popd

pushd trigger/virtcontainers
%gobuild
popd

%install
# install binaries
install -dp %{buildroot}%{_libexecdir}/%{repo}/trigger/virtcontainers
install -p -m 755 %{repo} %{buildroot}%{_libexecdir}/%{repo}
install -p -m 755 trigger/kicker/kicker %{buildroot}%{_libexecdir}/%{repo}/trigger/kicker
install -p -m 755 trigger/virtcontainers/virtcontainers %{buildroot}%{_libexecdir}/%{repo}/trigger/virtcontainers/vc

# install unitfiles
install -dp %{buildroot}%{_unitdir}
install -p -m 644 kata-%{repo}.service.in %{buildroot}%{_unitdir}/kata-%{repo}.service
install -p -m 644 kata-vc-throttler.service.in %{buildroot}%{_unitdir}/kata-vc-throttler.service

%check

%post
%systemd_post kata-vc-throttler

%preun
%systemd_preun kata-vc-throttler

%postun
%systemd_postun_with_restart kata-vc-throttler

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md OWNERS README.md
%dir %{_libexecdir}/%{repo}
%{_libexecdir}/%{repo}/%{repo}
%dir %{_libexecdir}/%{repo}/trigger
%dir %{_libexecdir}/%{repo}/trigger/virtcontainers
%{_libexecdir}/%{repo}/trigger/kicker
%{_libexecdir}/%{repo}/trigger/virtcontainers/vc
%{_unitdir}/kata-%{repo}.service
%{_unitdir}/kata-vc-throttler.service

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Pavel Mores <pmores@redhat.com> - 1.11.1-1
- Update to version 1.11.1

* Fri May 08 2020 Cole Robinson <crobinso@redhat.com> - 1.11.0-1
- Update to version 1.11.0

* Mon Apr 20 2020 Cole Robinson <aintdiscole@gmail.com> - 1.11.0-0.2.rc0
- Update to 1.11.0-rc0

* Tue Mar 31 2020 Cole Robinson <aintdiscole@gmail.com> - 1.11.0-0.1.alpha1
- Fix .service file issues

* Mon Mar 23 2020 Fabiano Fidêncio <fidencio@redhat.com> - 1.11.0-0.alpha1
- Update to release 1.11.0-alpha1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.10.0-1
- Update to release 1.10.0

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.3-1
- Update to release 1.9.3 (no changes upstream)

* Fri Jan 17 2020 Christophe de Dinechin <dinechin@redhat.com> - 1.9.2-1
- Update to release 1.9.2 (no changes upstream)

* Thu Nov 28 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.1-1
- Update to release 1.9.1

* Thu Nov 14 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.9.0-1
- Update to release 1.9.0

* Fri Sep 20 2019 Christophe de Dinechin <dinechin@redhat.com> - 1.8.2-1
- Update to 1.8.2 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3.git83ecff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2.git83ecff0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.4.1-1.git83ecff0
- bump to 1.4.1

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-4.git6e903fb
- build for all supported arches

* Wed Nov 21 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-3.git6e903fb
- Resolves: #1590417 - first official build
- make not needed as BR

* Mon Nov 12 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-2.git6e903fb
- bundled Provides

* Sat Nov 10 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.1-1.git6e903fb
- bump to v1.3.1
- built commit 6e903fb

* Thu Jun 14 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2.gitaa4d33d
- include scriptlets

* Thu Jun 14 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.gitaa4d33d
- first build (ready for Fedora review)
