Name:           ccd2iso
Version:        0.3
Release:        24%{?dist}
Summary:        CloneCD image to ISO image file converter

License:        GPLv2+
URL:            http://ccd2iso.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/ccd2iso/ccd2iso/ccd2iso-%{version}/ccd2iso-%{version}.tar.gz
# Fix compiler warnings.
# https://sourceforge.net/tracker/?func=detail&aid=3032074&group_id=94638&atid=608543
Patch0:         %{name}-%{version}-compilerWarnings.patch
# Add a manual page from debian distro.
# Sent upstream via email 20121201
Patch1:         %{name}-%{version}-manual.patch

#BuildRequires:  
#Requires:       

BuildRequires:  gcc
%description
The %{name} project converts CD backup files created using the non-free CloneCD
program to a format understood by most Free Software CD writing programs.


%prep
%setup -q
%patch0
%patch1
sed 's/\r//' TODO > TODO.tmp
touch -r TODO TODO.tmp
mv TODO.tmp TODO


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
rm INSTALL NEWS
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m644 ccd2iso.1 $RPM_BUILD_ROOT%{_mandir}/man1/ccd2iso.1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/ccd2iso.1



%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man1/ccd2iso.1.gz
%{_bindir}/%{name}



%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-10
- Adding a manual page from debian distro

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-6
- Removing the %%{name} macro from URL links

* Fri Jul 09 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-5
- Using the %%{name} macro throughout the whole file wherever applicable
- Adding a patch to address compiler warnings
- Fixing end-of-line errors in TODO directly in the %%prep section(without a
  patch)
- Excluding the INSTALL file from package contents
- Correcting the license to GPLv2+ to conform with the header notice in the
  source files

* Sun Apr 18 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-4
- Changing the license to reflect the right version of GPL
- Clarifying the patch purpose

* Wed Feb 17 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-3
- Using downloads.sourceforge.net instead of a mirror for Sourceforge URL in the
  Source0 field
- Adding  INSTALL="install -p" in the %%install section to preserve timestamps
- Fixing rpmlint errors

* Tue Feb 16 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-2
- Using %%{version} with the Source0 field

* Wed Jan 13 2010 Mohammed El-Afifi <Mohammed_ElAfifi@yahoo.com> - 0.3-1
- Initial RPM release
