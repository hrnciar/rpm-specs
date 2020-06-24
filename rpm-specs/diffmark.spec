Name:       diffmark
Version:    0.10
Release:    21%{?dist}
Summary:    XML diff and merge
# The library code has it's own license
# Parts of lib/lcs.hh is from Perl Algorithm::Diff module (GPL+ or Artistic)
# The build scripts are GPLv2+
License:    diffmark and GPLv2+ and (GPL+ or Artistic)
URL:        http://www.mangrove.cz/%{name}/
Source0:    %{url}%{name}-%{version}.tar.gz
# Superfluous RPATH in programs
Patch0:     %{name}-0.09-remove_rpath.patch
# Because of diffmark-0.08-remove_rpath.patch:
# And to update config.sub to support aarch64, bug #925255
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make

%description
This is a XML diff and merge package. It consists of a shared library and
two utilities: dm and dm-merge. 

%package        devel
Summary:        Development files for %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .rpath
# automake -i -f to support aarch64, bug #925255
libtoolize --force && autoreconf -i -f

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
make install "DESTDIR=$RPM_BUILD_ROOT"
find "$RPM_BUILD_ROOT" -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc doc/*.html README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Petr Pisar <ppisar@redhat.com> - 0.10-17
- Modernize spec file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Remi Collet <remi@fedoraproject.org> - 0.10-10
- rebuild with gcc 5 (thanks Koschei)

* Mon Feb 16 2015 Remi Collet <remi@fedoraproject.org> - 0.10-9
- rebuild with gcc 5 (thanks Koschei)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 0.10-5
- Update config.sub to support aarch64 (bug #925255)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Tue Nov 15 2011 Petr Pisar <ppisar@redhat.com> - 0.09-1
- 0.09 bump

* Thu Oct 27 2011 Petr Pisar <ppisar@redhat.com> - 0.08-1
- Version 0.08 packaged


