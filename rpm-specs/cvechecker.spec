# commit
# Use a commit newer than 3.8 for pulling in some bugfixes
%global _commit 0f1ae263b8279e8cca103cf28ae37ab20340ec04
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           cvechecker
Version:        3.8
Release:        8%{?dist}
Summary:        Tool for compare packages installed in your system with CVE database
License:        GPLv3
URL:            https://github.com/sjvermeu/cvechecker
#Source0:       %%{url}/archive/%%{_commit}/%%{_commit}.tar.gz
Source0:        https://raw.githubusercontent.com/wiki/sjvermeu/%{name}/releases/%{name}-%{version}.tar.gz
Patch1:         0001-Fixed-a-segfault-in-case-of-an-invalid-line-in-the-w.patch
Patch2:         0002-Fixed-missing-increment-in-line-number-in-case-of-a-.patch
Patch3:         0003-Last-addition-to-Changelog-now-use-git-commit-log.patch
Patch4:         0004-skip-lines-with-invalid-cpe-types-in-pullcves.patch
BuildRequires:  gcc
BuildRequires:  libconfig-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  xmlto

%description
The goal of cvechecker is to report about possible vulnerabilities on your
system, by scanning a list of installed software and matching results with the
CVE database.
This is not a bullet-proof method and you will have many false positives
(i.e.: vulnerability is fixed with a revision-release, but the tool isn't able
to detect the revision itself).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%configure --enable-sqlite3 --enable-mysql --localstatedir=%{_sharedstatedir}
sed -i 's/\/mysql/\/mariadb/g;s/-lmysqlclient/-lmariadb/g' Makefile
%build
%make_build

%install
%make_install PREFIX="%{_prefix}"  CONFDIR="%{buildroot}%{_sysconfdir}"
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml 
xmlto --skip-validation html-nochunks %{buildroot}%{_docdir}/cvechecker/userguide.xml
#/usr/share/doc/cvechecker/
install -Dm644 userguide.html  %{buildroot}%{_docdir}/cvechecker/userguide.html
install -Dm644 acknowledgements.html  %{buildroot}%{_docdir}/cvechecker/acknowledgements.html
rm -f %{buildroot}%{_docdir}/cvechecker/acknowledgements.xml %{buildroot}%{_docdir}/cvechecker/userguide.xml

%check
make check

%files
%doc README.md
%doc ChangeLog
%{_docdir}/cvechecker/acknowledgements.html
%{_docdir}/cvechecker/userguide.html
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cvechecker.conf
%{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%{_datadir}/cvechecker
%{_sharedstatedir}/cvechecker/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 3.8-5
- Rebuild for new libconfig

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Zamir SUN <sztsian@gmail.com> 3.8-2
- Change BuildRequires mariadb-devel to mariadb-connector-c-devel and openssl-devel
- Fixes BZ1494225

* Sat Aug 05 2017 Zamir SUN <sztsian@gmail.com> 3.8-1
- Update to upstream 3.8.
- Modify for mariadb-devel soname change.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Zamir SUN <sztsian@gmail.com> 3.7-3
- Remove Group tag from spec file

* Tue Jul 04 2017 Zamir SUN <sztsian@gmail.com> 3.7-2
- Add debuginfo package and fix some warning

* Tue Mar 14 2017 Zamir SUN <sztsian@gmail.com> 3.7-1
- initial package