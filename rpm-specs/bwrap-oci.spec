Summary: Run OCI containers with bubblewrap
Name: bwrap-oci
Version: 0.1.2
Release: 14%{?dist}
Source0: %{url}/archive/%{name}-%{version}.tar.gz
License: LGPLv2+
URL: https://github.com/projectatomic/bwrap-oci

Requires: bubblewrap
Provides: bubblewrap-oci
# We always run autogen.sh
BuildRequires: autoconf automake
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: libseccomp-devel
BuildRequires: libxslt
BuildRequires: bubblewrap
BuildRequires: docbook-style-xsl
BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)

%description
bwrap-oci uses Bubblewrap to run a container from an OCI spec file.

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules

%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Giuseppe Scrivano <gscrivan@redhat.com> 0.1.2
- new upstream release

* Fri Sep 02 2016 Giuseppe Scrivano <gscrivan@redhat.com> 0.1.1-4
- Fix rpm dependencies

* Fri Sep 02 2016 Giuseppe Scrivano <gscrivan@redhat.com> 0.1.1-3
- Initial RPM release
