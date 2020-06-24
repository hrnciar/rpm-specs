Name:           renameutils
Version:        0.12.0
Release:        16%{?dist}
Summary:        A set of programs to make renaming and copying of files easier

License:        GPLv3+
URL:            http://www.nongnu.org/renameutils
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
Patch0:         renameutils-0.12.0-install-typo.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  readline-devel
BuildRequires:  gettext
# Bundled library exception: https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib) = 20120423

%description
The file renaming utilities (renameutils for short) are a set of
programs designed to make renaming of files faster and less
cumbersome.

The file renaming utilities consists of five programs - qmv, qcp, imv,
icp and deurlname.

The qmv ("quick move") program allows file names to be edited in a
text editor. The names of all files in a directory are written to a
text file, which is then edited by the user. The text file is read and
parsed, and the changes are applied to the files.

The qcp ("quick cp") program works like qmv, but copies files instead
of moving them.

The imv ("interactive move") program, is trivial but useful when you
are too lazy to type (or even complete) the name of the file to rename
twice. It allows a file name to be edited in the terminal using the
GNU Readline library. icp copies files.

The deurlname program removes URL encoded characters (such as %20
representing space) from file names. Some programs such as w3m tend to
keep those characters encoded in saved files.


%prep
%setup -q
%patch0 -p1 -b .install-typo


%build
%configure
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"
%find_lang %{name}
%find_lang %{name}-gnulib


%files -f %{name}.lang -f %{name}-gnulib.lang
%doc README TODO COPYING NEWS AUTHORS
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-14
- Rebuild for readline 8.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.12.0-7
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Ben Boeckel <mathstuf@gmail.com> - 0.12.0-1
- Update to 0.12.0
- Mention bundled gnulib

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Michael Ploujnikov <ploujj@gmail.com> 0.10.0-3
- Made the summary more exact

* Thu Mar 19 2009 Michael Ploujnikov <ploujj@gmail.com> 0.10.0-2
- fixed timestamps
- added AUTHORS to documentation
- improved the URL
- removed readline from Requires
- properly handled locales

* Sun Mar 15 2009 Michael Ploujnikov <ploujj@gmail.com> 0.10.0-1
- Intial Fedora build
