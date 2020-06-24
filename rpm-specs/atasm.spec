Name:           atasm
Version:        1.08
Release:        4%{?dist}
Summary:        6502 cross-assembler

License:        GPLv2+
URL:            http://atari.miribilist.com/atasm/
# fedora-getsvn atasm https://svn.code.sf.net/p/atasm/code/trunk 100
# svn rev 100 == version 1.08
Source0:        atasm-svn100.tar.bz2

BuildRequires:  gcc
BuildRequires:  zlib-devel


%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macroassembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.


%prep
%setup -q -n %{name}


%build
pushd src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DZLIB_CAPABLE -DUNIX"
sed -e 's|%%DOCDIR%%|%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}|g' %{name}.1.in > %{name}.1
popd


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

pushd src
install -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
popd


%check
pushd tests
make test
popd


%files
%doc LICENSE VERSION.TXT atasm.blurb atasm.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dan Horák <dan[at]danny.cz> - 1.08-1
- update to 1.08

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07d-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Dan Horák <dan[at]danny.cz> - 1.07d-7
- spec file cleanup

* Sat Jul 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.07d-6
- Honor %%{_pkgdocdir} where available.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 25 2010 Dan Horák <dan[at]danny.cz> - 1.07d-1
- update to 1.07d

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr  7 2009 Dan Horák <dan[at]danny.cz> - 1.06-2
- don't compress the man page

* Thu Mar 19 2009 Dan Horák <dan[at]danny.cz> - 1.06-1
- update to 1.06

* Sun Oct  7 2007 Dan Horák <dan[at]danny.cz> - 1.05-0.1.beta
- initial Fedora version
