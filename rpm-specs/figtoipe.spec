Name:           figtoipe
Version:        20091205
Release:        22%{?dist}
Summary:        FIG to IPE conversion tool
#
# GPLv2, with an exception for the CGAL libraries.
License:        GPLv2+ with exceptions
#
URL:            http://ipe7.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ipe7/tools/%{name}-%{version}.tar.gz
Source1:        http://www.gnu.org/licenses/gpl-2.0.txt
BuildRequires:  gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel

%description
Figtoipe is a program that reads FIG files (as generated by
xfig) and generates an XML file readable by the Ipe editor.

%prep
%setup -q
sed -i -e 's/\r//' README figtoipe.cpp
chmod a-x README figtoipe.cpp

# extract the changelog from figtoipe.cpp
perl -ne 'if(m|\* Changes| .. m|\*/|) { m| \* (.*)| && print "$1\n";}' < figtoipe.cpp > CHANGES
# extract the license terms from figtoipe.cpp
perl -ne 'if(m|This file| .. m| USA.$|) { print;}' < figtoipe.cpp > LICENSE

cp %{SOURCE1} .

%build
%{__cxx} %{optflags} -o figtoipe figtoipe.cpp %{?__global_ldflags} -lz

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm0755 figtoipe %{buildroot}%{_bindir}
install -pm0644 figtoipe.1 %{buildroot}%{_mandir}/man1

%files
%doc CHANGES gpl-2.0.txt LICENSE README
%{_bindir}/figtoipe
%{_mandir}/man1/figtoipe.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20091205-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20091205-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20091205-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010  <Laurent.Rineau__fedora@normalesup.org> - 20091205-2
- Fix URL, following rules from https://fedoraproject.org/wiki/Packaging:SourceURL#Sourceforge.net

* Sun Jan 10 2010  <Laurent.Rineau__fedora@normalesup.org> - 20091205-1
- New upstream release
- Change the URL of Source0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080505-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080505-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May 19 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20080505-2
- Do not compress man pages during builds (done by rpm).

* Sat May 17 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20080505-1
- New upstream release.

* Fri May 16 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20071004-5
- Add a copy of the figtoipe.cpp header in license.txt

* Fri Feb 15 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20071004-4
- Add a license file.
- Fix the BR: zlib-devel

* Thu Feb 14 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20071004-3
- Extract the changelog from figtoipe.cpp

* Thu Feb 14 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20071004-2
- Add the man page.

* Tue Feb 12 2008 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 20071004-1
- Initial build for Fedora.

