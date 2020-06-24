Name:		xrdhttpvoms
Version:	0.2.5
Release:	7%{?dist}
Summary:	VOMS security extractor plugin for XrdHTTP
License:	ASL 2.0
URL:		https://svnweb.cern.ch/trac/lcgdm
# The source of this package was pulled from upstream's vcs. Use the
# following commands to generate the tarball:
# svn export http://svn.cern.ch/guest/lcgdm/xrdhttpvoms/tags/xrdhttpvoms_0_1_0 xrdhttpvoms-0.1.0
# tar -czvf xrdhttpvoms-0.1.0.tar.gz xrdhttpvoms-0.1.0
Source0:	%{name}-%{version}.tar.gz
ExcludeArch: i386
ExcludeArch: i686
ExcludeArch: %{arm}

%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildRequires:  gcc-c++
BuildRequires:	boost-devel >= 1.41.0
%else
BuildRequires:	boost141-devel
%endif
BuildRequires:	cmake
BuildRequires:	xrootd >= 4.0.0
BuildRequires:	xrootd-devel >= 4.0.0
BuildRequires:	xrootd-server-devel >= 4.0.0
BuildRequires:	voms-devel >= 2.0.10

Requires:	xrootd >= 4.0.0
Requires:	voms >= 2.0.10


%description
This package provides the VOMS security extractor plugin for XrdHTTP. Given
a working setup of XrdHTTP, this library will be able to extract the VOMS
information from the certificate presented by the client. The extracted
information will be available for other plugins to apply authorization rules.

%prep
%setup -q -n %{name}-%{version}

%build
ls -lR /usr/include/xrootd
%cmake . -DCMAKE_INSTALL_PREFIX=/ -DCMAKE_BUILD_TYPE=RelWithDebInfo 

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

make install DESTDIR=%{buildroot}

%files 
%{_libdir}/libXrdHttpVOMS-4.so*
%doc README RELEASE-NOTES
%license LICENSE

%ldconfig_scriptlets


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 1 2017 Fabrizio Furano <fabrizio.furano@cern.ch> - 0.2.5-2
- New upstream releasem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Fabrizio Furano <fabrizio.furano@cern.ch> - 0.2.4-2
- First epel release

