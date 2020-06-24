%global gcalmantag 4

Name:		gcal
Version:	4.1
Release:	7%{?dist}
Summary:	GNU Gregorian calendar program

License:	GPLv3+
URL:		http://www.gnu.org/software/gcal/
Source0:	ftp://ftp.gnu.org/gnu/gcal/%{name}-%{version}.tar.xz
# The man pages are not shipped in tarball but reside in the git repository
# at https://git.savannah.gnu.org/git/gcal.git
# To fetch the man pages from a clone of that repository, do:
# $ gcalmantag=4  # n.b. there is no 4.1 tag
# $ git archive --format=tar v${gcalmantag} -- doc/en/man | \
#     xz > gcal-man-v${gcalmantag}.tar.xz
Source1:	gcal-man-v%{gcalmantag}.tar.xz
Patch:		gcal-glibc-no-libio.patch
BuildRequires:  gcc
BuildRequires:	gettext, ncurses-devel
BuildRequires:  libunistring-devel
Requires(post): info
Requires(preun): info

# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)

%description
Gcal is a program for calculating and printing calendars.  Gcal
displays hybrid and proleptic Julian and Gregorian calendar sheets.
It also displays holiday lists for many countries around the globe.

%prep
%setup -q
%patch -p1
tar xf %{SOURCE1}


%build
CFLAGS="%{optflags}"
export CFLAGS
export LIBS=-lunistring
%configure --enable-unicode
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 doc/en/man/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_datadir}/%{name}/Makefile.in
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS COPYING LIMITATIONS NEWS README THANKS TODO
%{_bindir}/gcal
%{_bindir}/gcal2txt
%{_bindir}/tcal
%{_bindir}/txt2gcal
%{_datadir}/gcal/
%{_infodir}/*.info*
%{_mandir}/man1/*.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug  3 2018 Daiki Ueno <dueno@redhat.com> - 4.1-4
- Fix FTBFS with glibc 2.28

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug  6 2017 Matthew Miller <mattdm@fedoraproject.org> - 4.1-1
- new upstream minor release
- enable unicode, because it's 2017
- change man page to xz

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Daiki Ueno <dueno@redhat.com> - 4-1
- new upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun  4 2014 Daiki Ueno <dueno@redhat.com> - 3.6.3-1
- new upstream release (#100912)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep  3 2012 Daiki Ueno <dueno@redhat.com> - 3.6.2-3
- add ncurses-devel to BR to build with highlighting support (#853655)
- change Group to Application/Productivity (thanks Matthew Miller for
  the suggestion)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Daiki Ueno <dueno@redhat.com> - 3.6.2-1
- new upstream release
- add "Provides: bundled(gnulib)" (#821755)
- minor cleanup of the spec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 17 2011 Daiki Ueno <dueno@redhat.com> - 3.6-3
- add Group: tag
- use %%optflags when building

* Tue May 17 2011 Daiki Ueno <dueno@redhat.com> - 3.6-2
- fetch man pages from the git repo

* Thu May 12 2011 Daiki Ueno <dueno@redhat.com> - 3.6-1
- initial packaging for Fedora

