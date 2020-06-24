%define    profiledir    %{_sysconfdir}/profile.d

Name:       cdargs
Version:    1.35
Release:    24%{?dist}
Summary:    The shell cd with bookmarks and browser
License:    GPLv2+
URL:        http://www.skamphausen.de/cgi-bin/ska/CDargs/
Source0:    http://www.skamphausen.de/downloads/cdargs/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}_emacs-init.el

Patch0:     %{name}-%{version}_shebangs.patch
Patch1:     %{name}-%{version}_format_security.patch
Patch2:     %{name}-%{version}_fix_fsf_address.patch

BuildRequires:    gcc-c++
BuildRequires:    ncurses-devel
BuildRequires:    emacs
Requires:         emacs-filesystem >= %{_emacs_version}

%description
Enables the user to quickly change working directory by navigating cd arguments
and expanding the shell built-in cd with bookmarks and browser.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.


%prep
%autosetup -p1


%build
%configure
%make_build
%{_emacs_bytecompile} contrib/cdargs.el


%install
%make_install

mkdir -p %{buildroot}%{profiledir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}

install -p -m 644 contrib/cdargs.el* %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/cdargs-init.el

install -p -m 644 contrib/cdargs-bash.sh %{buildroot}%{profiledir}/cdargs.sh
install -p -m 644 contrib/cdargs-tcsh.csh %{buildroot}%{profiledir}/cdargs.csh
install -D -p -m 644 src/cdargs.h %{buildroot}%{_includedir}/cdargs.h


%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/cdargs
%config(noreplace) %{profiledir}/cdargs.*
%doc %{_mandir}/man1/cdargs.1*
%dir %{_emacs_sitelispdir}/%{name}
%{_emacs_sitelispdir}/%{name}/*.el
%{_emacs_sitelispdir}/%{name}/*.elc
%{_emacs_sitestartdir}/cdargs-init.el


%files devel
%{_includedir}/cdargs.h


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 20:25:44 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.35-22
- Remove emacs subpackage to conform with Emacs packaging guidelines (#1234562)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Tim Landscheidt <tim@tim-landscheidt.de> - 1.35-20
- Obsolete emacs-el subpackage (#1234562)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.35-18
- Unorphaned
- Refresh SPEC

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.35-16
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.35-14
- Fix FTBFS with -Werror=format-security (#1037010, #1106037)
- Cleanup spec

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-9
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.35-6
- Update spec file to bring it into compliance with Emacs add-on packaging
  guidelines
- Split Elisp source files into separate subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Sun Jan 11 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 1.35-3
- Fixed usage in other shells than bash: minor compatibility code changes and
  no complains because completion doesn't work (fix BZ#479398).

* Tue Mar 25 2008 Milos Jakubicek <xjakub@fi.muni.cz> - 1.35-2
- Fixed non-capital starting letter in the summary of emacs-cdargs subpackage.

* Sat Mar 08 2008 Milos Jakubicek <xjakub@fi.muni.cz> - 1.35-1
- Initial package based on SRPM provided by author.
- Removed Packager: and Vendor: field.
- Removed unnecessary making RPM_BUILD_ROOT directory.
- Changed license from GPL to GPLv2+.
- Extended description.
- Setup section is silent now (-p).
- Added SMP flags for building.
- Added directory mode to defattr.
- Added dist tag.
- Changed buildroot directory to default.
- Removed execute rights and shebangs (Patch0) from cdargs.sh, cdargs.csh as
  they will be only sourced, not executed.
- Both files cdargs.sh and cdargs.csh marked as config(noreplace).
- Added -devel subpackage with cdargs.h
- Added emacs-cdargs subpackage with cdargs.el
- Added emacs init script as Source1
