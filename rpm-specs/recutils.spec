Name:		recutils
Version:	1.7
Release:	17%{?dist}
Summary:	A set of tools to access GNU recfile databases

License:	GPLv3+
URL:		http://www.gnu.org/software/recutils/
Source0:	ftp://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz
Source1:	rec-mode-init.el
Patch0:		recutils-shared-lib-calls-exit.patch
Patch1:		recutils-Wformat.patch
# http://git.savannah.gnu.org/cgit/gnulib.git/commit/?id=4af4a4a71827c0bc5e0ec67af23edef4f15cee8e
Patch2:		recutils-glibc-no-libio.patch
# http://git.savannah.gnu.org/cgit/recutils.git/commit/etc/rec-mode.el?id=a917dfc0c376a9d7b47f6556f27687a17cde4298
Patch3:		recutils-rec-mode-fixes.patch

BuildRequires:  gcc
BuildRequires:	gettext
BuildRequires:	emacs-nox
BuildRequires:	chrpath
BuildRequires:	libgcrypt-devel
BuildRequires:	help2man
BuildRequires:	mdbtools-devel
BuildRequires:	texinfo
Requires:	emacs(bin) >= %{_emacs_version}
# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)

%description
Recutils is a set of tools and libraries to access human-editable,
text-based databases called recfiles. The data is stored as a sequence
of records, each record containing an arbitrary number of named
fields.

%package devel
Summary:	Libraries and header files for recutils
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and header files for recutils


%prep
%setup -q
%patch0 -p1 -b .shared-lib-calls-exit
%patch1 -p1 -b .Wformat
%patch2 -p0 -b .glibc-no-libio
%patch3 -p1 -b .rec-mode-fixes

%build
%configure --disable-static --disable-rpath
make %{?_smp_mflags}
%{_emacs_bytecompile} etc/rec-mode.el


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

# install Emacs mode
install -dm 755 %{buildroot}%{_emacs_sitelispdir}
install -pm 644 etc/rec-mode.el* %{buildroot}%{_emacs_sitelispdir}
# by default, the Emacs mode is installed under datadir.
rm -f %{buildroot}%{_datadir}/rec-mode.el

# install startup file for the Emacs mode installed above
install -dm 755 %{buildroot}/%{_emacs_sitestartdir}/
install -pm 644 %{SOURCE1} %{buildroot}/%{_emacs_sitestartdir}/

rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

chrpath --delete %{buildroot}%{_bindir}/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/recutils
%{_infodir}/*.info*
%{_emacs_sitelispdir}/*.el*
%{_emacs_sitestartdir}/*.el

%files devel
%{_includedir}/rec.h
%{_libdir}/*.so


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 1.7-15
- Depend on texinfo in case docs need to get rebuilt

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug  3 2018 Daiki Ueno <dueno@redhat.com> - 1.7-12
- Fix FTBFS with glibc 2.28
- Fix rec-mode.el typo

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Daiki Ueno <dueno@redhat.com> - 1.7-2
- add mdbtools-devel to BR (#1099444)

* Thu Mar 27 2014 Daiki Ueno <dueno@redhat.com> - 1.7-1
- new upstream release
- add recutils-Wformat.patch
- pull help2man

* Thu Nov  7 2013 Daiki Ueno <dueno@redhat.com> - 1.6-1
- new upstream release
- drop no_gets patch which is no longer necessary

* Mon Aug 26 2013 Daiki Ueno <dueno@redhat.com> - 1.5-7
- pull libgcrypt-devel for encryption support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.5-4
- Fix gets call for glibc-2.16 changes

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Daiki Ueno <dueno@redhat.com> - 1.5-2
- add "Provides: bundled(gnulib)" (#821787)

* Mon Feb 20 2012 Daiki Ueno <dueno@redhat.com> - 1.5-1
- new upstream release
- remove %%defattr(-,root,root,-) from %%files

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Daiki Ueno <dueno@redhat.com> - 1.4-1
- new upstream release
- remove recutils-recfix-size-lp64.patch since it is applied in upstream

* Tue Oct 18 2011 Daiki Ueno <dueno@redhat.com> - 1.3-4
- add recutils-shared-lib-calls-exit.patch
- merge -libs subpackage into the base package

* Tue Oct 18 2011 Daiki Ueno <dueno@redhat.com> - 1.3-3
- use chrpath instead of patching libtool, so that the programs used
  in %%check can find librec.so

* Tue May 17 2011 Daiki Ueno <dueno@redhat.com> - 1.3-2
- run test suite when building

* Thu May 12 2011 Daiki Ueno <dueno@redhat.com> - 1.3-1
- initial packaging for Fedora

