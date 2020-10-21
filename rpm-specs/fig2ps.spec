Name:           fig2ps
Version:        1.5
Release:        16%{?dist}
Summary:        Utility for converting xfig pictures to PS/PDF
License:        GPLv2+
URL:            http://fig2ps.sourceforge.net/
Source0:        http://downloads.sourceforge.net/fig2ps/%{name}-%{version}.tar.bz2
Patch0:         fig2ps-1.5-gv-ps-fix.patch
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)

Requires:       tex(latex) tex(dvips) ghostscript gv transfig

%description
fig2ps is a perl script which converts xfig files to postscript or
PDF, using LaTeX for processing text (a capability not included in
transfig). This provides the benefit of seamless integration of
figures into documents (the font in the figures is the same as in the
text), and allows for special typesetting commands (such as
mathematical equations) to be included in figures.


%prep
%setup -q
%patch0 -p1


%build


%install
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc


%files
%doc ChangeLog README examples
%license GPL.txt
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) /etc/fig2ps


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5-8
- Add perl-BRs (F24FTBFS).
- Add %%license.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Hans de Goede <hdegoede@redhat.com> - 1.5-1
- New upstream version 1.5
- Switch to new tex general dependencies (rhbz#836901)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Stepan Kasal <skasal@redhat.com> - 1.4.1-1
- new upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.3.6-3
- fix license tag

* Thu Jan 25 2007 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.6-2
- Fix broken source URL.

* Thu Jan 25 2007 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.6-1
- New release.

* Fri Sep 15 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.5-3
- Rebuild for FC6.

* Fri May 12 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.5-2
- Add gv as a dependency.
- Add dist tag.

* Mon Jan 16 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.5-1
- New upstream release

* Wed Sep 21 2005 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.3-2
- fix make install command

* Tue Sep 20 2005 Quentin Spencer <qspencer@users.sourceforge.net> 1.3.3-1
- Initial version.
