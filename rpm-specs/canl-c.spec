Name:           canl-c
Version:        3.0.0
Release:        8%{?dist}
Summary:        EMI Common Authentication library - bindings for C

License:        ASL 2.0
URL:            http://www.eu-emi.eu
Source:         http://scientific.zcu.cz/emi/emi.canl.c/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel >= 1.1
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig
BuildRequires:  tex(latex)
BuildRequires:  tex(lastpage.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(ptmr7t.tfm)
BuildRequires:  tex(phvr8t.tfm)
BuildRequires:  tex(psyr.tfm)
BuildRequires:  tex(pzcmi8r.tfm)
BuildRequires:  tex(ucrr8a.pfb)

%description
This is the C part of the EMI caNl -- the Common Authentication Library.


%package        devel
Summary:        Development files for EMI caNl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       krb5-devel%{?_isa}

%description    devel
This package contains development libraries and header files for EMI caNl.


%package        doc
Summary:        API documentation for EMI caNl
BuildArch:      noarch

%description    doc
This package contains API documentation for EMI caNl.


%package        examples
Summary:        Example programs of EMI caNl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
This package contains client and server examples of EMI caNl.


%prep
%setup -q


%build
./configure --root=/ --prefix=%{_prefix} --libdir=%{_lib}
CFLAGS="%{?optflags}" LDFLAGS="%{?__global_ldflags}" make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
# in -doc subpackage
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/README
rm -f %{buildroot}%{_defaultdocdir}/%{name}-%{version}/canl.pdf
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la


%ldconfig_scriptlets


%files
%license LICENSE
%doc ChangeLog README
%{_libdir}/libcanl_c.so.4
%{_libdir}/libcanl_c.so.4.*

%files devel
%{_includedir}/*.h
%{_libdir}/libcanl_c.so

%files doc
%license LICENSE
%doc canl.pdf

%files examples
%{_bindir}/*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-1
- Major version bump
- OpenSSL 1.1 (fixed  #1423249)
- Removed EPEL macros (branch 3.x.x only for openssl >= 1.1 and F26+)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 František Dvořák <valtri@civ.zcu.cz> - 2.1.7-1
- New upstream version
- %%license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.6-1
- New upstream version
- Removed gcc 4.9.0 patch merged upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.5-1
- New upstream version
- Consistent style with buildroot macro
- Patch to build with gcc 4.9.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.4-1
- New upstream version
- Remove patch merged in upstream

* Wed Jan 29 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.3-2
- Patch to remove comment.sty LaTeX package (not available on RHEL7)

* Thu Jan 16 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.3-1
- New upstream version
- Removed arch-specific BuildRequires
- EPEL 7 support
- Enabled parallel build
- Removed %%check target
- Replaced find command by wildcards

* Thu Aug 08 2013 František Dvořák <valtri@civ.zcu.cz> - 2.1.2-1
- New upstream version
- Proper perl usage
- Added README file

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 František Dvořák <valtri@civ.zcu.cz> - 2.1.1-1
- New upstream version

* Thu Jan 31 2013 František Dvořák <valtri@civ.zcu.cz> - 2.0.7-1
- New upstream version
- Move API documentation to subpackage (devel subpackage multilib now)

* Tue Jan 22 2013 František Dvořák <valtri@civ.zcu.cz> - 2.0.3-1
- Initial package
