Name:		gimp-fourier-plugin
Version:	0.4.1
Release:	22%{?dist}
Summary:	A simple plug-in to do fourier transform on your image

License:	GPLv3+
URL:		http://people.via.ecp.fr/~remi/soft/gimp/gimp_plugin_en.php3
Source0:	http://people.via.ecp.fr/~remi/soft/gimp/fourier-%{version}.tar.gz
Patch0:		gimp-fourier-plugin.build.patch

BuildRequires:  gcc
BuildRequires:	gimp-devel
BuildRequires:	fftw3-devel
BuildRequires:	dos2unix
Requires:	gimp


%description
A simple plug-in to do fourier transform on your image. The major advantage of 
this plugin is to be able to work with the transformed image inside GIMP.


%prep
%setup -q -n fourier-%{version}
%patch0 -p1 -b .build

# Fix for wrong-file-end-of-line-encoding problem
dos2unix README
dos2unix README.Moire

# Fix utf-8 encoding
iconv -f ISO-8859-1 -t UTF-8 README > README.utf8
iconv -f ISO-8859-1 -t UTF-8 README.Moire > README.Moire.utf8


%build
export GCC="gcc %{optflags}"
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_libdir}/gimp/2.0/plug-ins/
install fourier %{buildroot}/%{_libdir}/gimp/2.0/plug-ins/


%files
%doc README.utf8 README.Moire.utf8
%{_libdir}/gimp/2.0/plug-ins/fourier


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.4.1-9
- Fix FTBFS due to missing -lm (#1106621)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 0.4.1-4
- rebuild against gimp 2.8.0 release candidate

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 0.4.1-2
- rebuild for GIMP 2.7

* Wed Aug 31 2011 Fabian Deutsch <fabiand@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Fabian Deutsch <fabian.deutsch at gmx.de> 0.3.2-2
- Fix UTF-8
- Using optflags

* Mon Jan 19 2009 Fabian Deutsch <fabian.deutsch at gmx.de> 0.3.2-1
- Updated to 0.3.2
- Includes license note
- Small hack around gimptool-2.0 bug.

* Sun Dec 07 2008 Fabian Deutsch <fabian.deutsch at gmx.de> 0.3.1-1
- Version 0.3.1
- Initial.
