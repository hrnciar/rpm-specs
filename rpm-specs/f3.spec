Name:		f3
Version:	7.0
Release:	6%{?dist}
Summary:	Utility to test for fake flash drives and cards
License:	GPLv3
URL:		http://oss.digirati.com.br/%{name}/
Source0:	https://github.com/AltraMayor/%{name}/archive/v%{version}/%{name}-%{version}.zip

BuildRequires:  gcc
BuildRequires:  systemd-devel
BuildRequires:  parted-devel


%description
F3 is a utility to test for fake flash drives and cards. It is a Free
Software alternative to h2testw.  f3write will fill the unused part of
a filesystem with files NNNN.fff with known content, and f3read will
analyze the files to determine whether the contents are corrupted, as
happens with fake flash.

%prep
%setup -q
sed -i -e 's/gcc/gcc $(CFLAGS)/' Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" all extra

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 f3read f3write f3probe f3brew f3fix %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 f3read.1 %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%doc README.rst
%{_bindir}/f3read
%{_bindir}/f3write
%{_bindir}/f3brew
%{_bindir}/f3fix
%{_bindir}/f3probe
%{_mandir}/man1/f3read.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Eric Smith <brouhaha@fedoraproject.org> 7.0-1
- Update to latest upstream release.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Eric Smith <brouhaha@fedoraproject.org> 5.0-1
- Update to latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jun 22 2012 Eric Smith <eric@brouhaha.com>  2-2
- Updated based on package review comments

* Wed Apr 25 2012 Eric Smith <eric@brouhaha.com>  2-1
- Initial version
