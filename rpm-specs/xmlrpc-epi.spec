Name:      xmlrpc-epi
Version:   0.54.2
Release:   11%{?dist}
Summary:   An implementation of the XML-RPC protocol in C
License:   MIT
URL:       http://xmlrpc-epi.sourceforge.net/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:    0000-fix-printf-formatting-security.patch
Patch1:    0001-fix-heap-buffer-overflow-CVE-2016-6296.patch
BuildRequires:  gcc
BuildRequires: expat-devel

%description
An implementation of the XML-RPC protocol in C.

%package  devel
Summary:  Development files for xmlrpc-epi
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The xmlrpc-epi-devel package contains libraries and header files for
developing applications that use xmlrpc-epi.

%prep
%setup -q

%patch0 -p1 -b .fix-printf-formatting-security
%patch1 -p1 -b .fix-heap-buffer-overflow-CVE-2016-6296

%build
%configure --disable-static --includedir=%{_includedir}/xmlrpc-epi
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

# Remove the sample test tools
rm -r %{buildroot}%{_bindir}

rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/libxmlrpc-epi.so.0*

%files devel
%{_includedir}/xmlrpc-epi
%{_libdir}/libxmlrpc-epi.so

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 0.54.2-6
- Rebuild with binutils fix for ppc64le (#1475636)

* Tue Jul 25 2017 Shawn Starr <spstarr@fedoraproject.org> - 0.54.2-5
- Fix CVE-2016-6296, adapted from PHP upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jul 19 2014 Shawn Starr <shawn.starr@rogers.com> - 0.54.2-1
- Un-orphan package, update to latest release, fix compile issues
- Fix up spec from initial review

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.54.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 20 2010 Bryan O'Sullivan <bos@serpentine.com> 0.54.1-2
- A few small changes requested during packaging review for bz 539388.

* Thu Nov 19 2009 Bryan O'Sullivan <bos@serpentine.com> 0.54.1-1
- Initial build of 0.54.1, based on Callum Lerwick's abandoned spec
  file from a few years ago.
