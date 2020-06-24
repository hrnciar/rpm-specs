Name:           wdiff
Version:        1.2.2
Release:        14%{?dist}
Summary:        A front-end to GNU diff

License:        GPLv3+
URL:            http://www.gnu.org/software/%{name}/
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool  
BuildRequires:  texinfo  

#https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 30.5.2012

%description
`wdiff' is a front-end to GNU `diff'.  It compares two files, finding
which words have been deleted or added to the first in order to create
the second.  It has many output formats and interacts well with
terminals and pagers (notably with `less').  `wdiff' is particularly
useful when two texts differ only by a few words and paragraphs have
been refilled.

%prep
%setup -q -n %{name}-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && \
mv ChangeLog.new ChangeLog

%build
%configure --enable-experimental="mdiff wdiff2 unify" 
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name '*gnulib.mo' -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS  README TODO  ChangeLog  AUTHORS
%{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_infodir}/%{name}.info.*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.2-12
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.2.2-1
- New release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.2.1-1
- New release 

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1.2-1
- New release and fixed no bundled library issue

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.1.0-1
- New release

* Thu Oct 20 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-1
- New release

* Thu Sep 8 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.0-1
- New release

* Fri Mar 4 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-5
- Fix change log issue 

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-4
- Add find language tag

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-3
- Removed unnecessary -gnulib translation files.
- Rpmlint warning fixed for ChangeLog not utf8 file.
- Adding %%doc files

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-2
- Fix license,buildroot issue. Add find language tag.

* Tue Mar 1 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 0.6.5-1
- Initial version of the package
