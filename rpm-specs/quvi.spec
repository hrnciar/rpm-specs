Name:           quvi
Version:        0.9.5
Release:        13%{?dist}
Summary:        Command line tool for parsing video download links
License:        AGPLv3+
URL:            http://quvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libquvi-devel
BuildRequires:  libxml2-devel

%description
quvi is a command line tool for parsing video download links.
It supports Youtube and other similar video websites.
libquvi is a library for parsing video download links with C API.
It is written in C and intended to be a cross-platform library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc ChangeLog COPYING README 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}rc.5*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 28 2013 Christopher Meng <rpm@cicku.me> - 0.9.5-1
- New version.

* Fri Aug 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.3.1-1
- Update to 0.9.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 11 2012 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.2-1
- Update to 0.4.2

* Fri Dec  2 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.1-1
- Update to 0.4.1

* Tue Nov 15 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-2
- Add libcurl dependancy

* Sat Oct  8 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.4.0-1
- Update to 0.4.0

* Mon Aug 15 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.19-1
- Update to 0.2.19

* Mon Jul 25 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.18-1
- Update to 0.2.18

* Fri Jun 24 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.17-1
- Update to 0.2.17

* Sun May 22 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.16-1
- Update to 0.2.16
- enable-smut option changed to enable-nsfw

* Sat Apr 23 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.15-1
- Update to 0.2.15

* Sun Mar 13 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.14-1
- Update to 0.2.14

* Thu Feb 17 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.13-1
- Update to 0.2.13

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.12-1
- Update to 0.2.12
- Licence changed to LGPLv2+

* Tue Dec 14 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.10-1
- Update to 0.2.10

* Sun Nov 14 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.8-1
- Update to 0.2.8

* Thu Oct 28 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.7-1
- Update to 0.2.7

* Tue Oct 12 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.6-1
- Update to 0.2.6

* Sat Oct  2 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.5-1
- Update to 0.2.5

* Fri Sep 10 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.4-1
- Update to 0.2.4

* Sun Sep  5 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.3-1
- Update to 0.2.3

* Wed Aug 25 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.2-1
- Update to 0.2.2

* Fri May  7 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.2.0-1
- Update to 0.2.0

* Mon Apr  5 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.4-1
- Update to 0.1.4

* Fri Apr  2 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.3-3
- Removed redundant option for post and postun
- Append slashes to directories in files section
- Add blanks lines between changelog revisions

* Thu Apr  1 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.3-2
- License fix
- Merged libquvi and quvi packages

* Tue Mar 30 2010 Nicoleau Fabien <nicoleau.fabien@gmail.com> 0.1.3-1
- Initial build
