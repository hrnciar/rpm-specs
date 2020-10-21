%global srcname lib-zfcp-hbaapi

Name:           libzfcphbaapi
Summary:        HBA API for the zFCP device driver
Version:        2.2.0
Release:        7%{?dist}
License:        CPL
URL:            http://www.ibm.com/developerworks/linux/linux390/zfcp-hbaapi.html
# http://www.ibm.com/developerworks/linux/linux390/zfcp-hbaapi-%%{hbaapiver}.html
Source0:        http://download.boulder.ibm.com/ibmdl/pub/software/dw/linux390/ht_src/%{srcname}-%{version}.tar.gz
Patch1:         %{srcname}-2.1.1-fedora.patch

ExclusiveArch:  s390 s390x

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libsysfs-devel
BuildRequires:  sg3_utils-devel
BuildRequires:  libhbaapi-devel
Requires:       libhbaapi
Requires(post): grep sed
Requires(postun): grep sed

# exclude plugin soname from Provides
%global __provides_exclude ^(libzfcphbaapi-%{version}[.]so.*)$

%description
zFCP HBA API Library is an implementation of FC-HBA (see www.t11.org) for
the zFCP device driver.


%package docs
License:  CPL
Summary:  zFCP HBA API Library -- Documentation
URL:      http://www.ibm.com/developerworks/linux/linux390/zfcp-hbaapi.html
Requires: %{name} = %{version}-%{release}
Provides:       s390utils-libzfcphbaapi-docs = 2:1.20.0-4
Obsoletes:      s390utils-libzfcphbaapi-docs <= 2:1.20.0-3

%description docs
Documentation for the zFCP HBA API Library.


%prep
%setup -q -n %{srcname}-%{version}

%patch1 -p1 -b .fedora


%build
%configure --disable-static --enable-vendor-lib
make EXTRA_CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"


%install
%makeinstall docdir=$RPM_BUILD_ROOT%{_docdir}/%{name}
# keep only html docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/latex
# remove unwanted files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.*


%post
# remove old entry from hba.conf on upgrade
if [ $1 == 2 ]; then
    grep -q -e "^libzfcphbaapi" /etc/hba.conf &&
        sed -i.orig -e "/^libzfcphbaapi/d" /etc/hba.conf
fi
# add entry to hba.conf on install and upgrade (resulting in a refresh together with ^)
# the grep ensures there won't be a duplicate entry after reinstall
grep -q -e "^libzfcphbaapi" /etc/hba.conf ||
    echo "libzfcphbaapi %{_libdir}/libzfcphbaapi-%{version}.so" >> /etc/hba.conf
:

%postun
# remove entry from hba.conf on uninstall
if [ $1 == 0 ]; then
    grep -q -e "^libzfcphbaapi" /etc/hba.conf &&
        sed -i.orig -e "/^libzfcphbaapi/d" /etc/hba.conf
fi
:


%files
%doc README COPYING ChangeLog AUTHORS LICENSE
%{_bindir}/zfcp_ping
%{_bindir}/zfcp_show
%{_libdir}/%{name}-%{version}.so
%{_mandir}/man3/libzfcphbaapi.3*
%{_mandir}/man3/SupportedHBAAPIs.3*
%{_mandir}/man3/UnSupportedHBAAPIs.3*
%{_mandir}/man8/zfcp_ping.8*
%{_mandir}/man8/zfcp_show.8*
%exclude %{_mandir}/man3/hbaapi.h.3*
%exclude %{_docdir}/%{name}/html


%files docs
%{_docdir}/%{name}/html


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Dan Horák <dan@danny.cz> - 2.2.0-6
- rebuilt for sg3_utils 1.45 (#1809392)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Dan Horák <dan[at]danny.cz> - 2.2.0-4
- fix scriptlets so they work correctly on upgrades

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.2.0-2
- Fix requirement for %%preun (instead of %%postun) scriptlet

* Thu Feb 28 2019 Dan Horák <dan[at]danny.cz> - 2.2.0-1
- updated to 2.2.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Dan Horák <dan@danny.cz> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Dan Horák <dan[at]danny.cz> - 2.1.1-1
- updated to 2.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Dan Horák <dan[at]danny.cz> - 2.1-2
- add missing compatibility Provides
- exclude plugin soname from Provides

* Thu May 16 2013 Dan Horák <dan[at]danny.cz> - 2.1-1
- move libzfcphbaapi to own package from s390utils
