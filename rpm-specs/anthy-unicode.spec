%global pkg  anthy-unicode
%bcond_with xemacs
%bcond_without autoreconf

Name:  anthy-unicode
Version: 1.0.0.20191015
Release: 5%{?dist}
# The entire source code is LGPLv2+ and dictionaries is GPLv2. the corpus data is under Public Domain.
License: LGPLv2+ and GPLv2 and Public Domain
URL:  https://github.com/fujiwarat/anthy-unicode/wiki
BuildRequires: emacs
BuildRequires: gcc
BuildRequires: git
%if 0%{?rhel} == 0
BuildRequires: xemacs
%endif
%if %{with autoreconf}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif

Source0: https://github.com/fujiwarat/anthy-unicode/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-init.el
# Upstreamed patches
#Patch0: %%{name}-HEAD.patch
Patch0: %{name}-HEAD.patch

Summary: Japanese character set input library for Unicode

%description
Anthy Unicode is another Anthy project and provides the library to input
Japanese on the applications, such as X applications and emacs. and the
user dictionaries and the users information which is used for the conversion,
is stored into their own home directory. So Anthy Unicode is secure than
other conversion server.

%package -n emacs-%{pkg}
Summary: Emacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: emacs(bin) >= %{_emacs_version}
BuildArch: noarch

%description -n emacs-%{pkg}
This package contains the byte compiled elips packages to run %{pkg}
with GNU Emacs.

%if 0%{?rhel} == 0
%package -n xemacs-%{pkg}
Summary: XEmacs files for %{pkg}
Requires: %{name} = %{version}-%{release}
Requires: xemacs(bin) >= %{_xemacs_version}
BuildArch: noarch

%description -n xemacs-%{pkg}
This package contains the elips packages to run %{pkg} with GNU XEmacs.
%endif

%package devel
Summary: Header files and library for developing programs which uses Anthy Unicode
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The anthy-devel package contains the development files which is needed to build
the programs which uses Anthy Unicode.


%prep
%autosetup -S git

%build
%if %{with autoreconf}
autoreconf -f -i -v
%endif
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove unnecessary files
rm $RPM_BUILD_ROOT%{_libdir}/lib*.la

## for emacs-anthy
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}

%if 0%{?rhel} == 0
## for xemacs-anthy
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
# FIXME lisp build
%if %{with xemacs}
pushd $RPM_BUILD_DIR/%{name}-%{version}/src-util
make clean
make EMACS=xemacs lispdir="%{_xemacs_sitelispdir}/%{pkg}"
make install-lispLISP DESTDIR=$RPM_BUILD_ROOT EMACS=xemacs lispdir="%{_xemacs_sitelispdir}/%{pkg}" INSTALL="install -p"
popd
%else
mkdir -p $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}
cp $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/*.el \
   $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/.
%endif
%endif

%check
cd test
env LD_LIBRARY_PATH=../src-main/.libs:../src-worddic/.libs ./anthy --all
env LD_LIBRARY_PATH=../src-main/.libs:../src-worddic/.libs ./checklib

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog DIARY NEWS README
%license COPYING
%{_bindir}/*
# If new keywords are added in conf files, "noreplace" flag needs to be deleted
%config(noreplace) %{_sysconfdir}/*.conf
%{_libdir}/lib*.so.*
%{_datadir}/%{pkg}/

%files -n emacs-%{pkg}
%doc doc/ELISP
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%dir %{_emacs_sitelispdir}/%{pkg}

%if 0%{?rhel} == 0
%files -n xemacs-%{pkg}
%doc doc/ELISP
%{_xemacs_sitelispdir}/%{pkg}/*.el
%if %{with xemacs}
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%endif
%{_xemacs_sitestartdir}/*.el
%dir %{_xemacs_sitelispdir}/%{pkg}
%endif

%files devel
%doc doc/DICLIB doc/DICUTIL doc/GLOSSARY doc/GRAMMAR doc/GUIDE.english doc/ILIB doc/LEARNING doc/LIB doc/MISC doc/POS doc/SPLITTER doc/TESTING doc/protocol.txt
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.20191015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20191015-2
- Add %%check to run local test programs

* Tue Oct 15 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20191015-1
- Release anthy-unicode 1.0.0.20191015

* Wed Aug 07 2019 Takao Fujiwara <fujiwara@redhat.com> 1.0.0.20190412-1
- Initial package
- Update license
- Delete Group tags
- Make parse_modify_freq_command() for UTF-8
- Revert ptab.h to EUC-JP
- BuildRequire: git
- Genearate emacs- and xemacs- sub packages
- Fix some obsolete warnings in emacs batch-byte-compile
- Fix shared-lib-calls-exit
- Fix non-conffile-in-etc
- Fix description-line-too-long
