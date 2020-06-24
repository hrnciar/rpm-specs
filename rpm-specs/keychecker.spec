Name:           keychecker
Version:        1.0
Release:        8%{?dist}
Summary:        Generate list of installed packages sorted by GPG key
License:        GPLv2+
URL:            https://github.com/jds2001/keychecker
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch
%if 0%{?fedora}
Requires:       python3-rpm
%else
Requires:       rpm-python
%endif
%if 0%{?rhel} && 0%{?rhel} <= 6
Requires:       python-argparse
%endif


%description
Separately list rpm's based on the GPG key they were signed with


%prep
%setup -q
%if 0%{?fedora}
sed -e '1 s|python|python3|' -i key_checker.py
%endif


%install
install -Dpm 0755 key_checker.py %{buildroot}%{_bindir}/keychecker


%files
%license LICENSE
%doc README known_keys.txt
%{_bindir}/keychecker


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Carl George <carl@george.computer> - 1.0-3
- Use python3 on Fedora
- Add requirement for python rpm module
- Properly handle license file

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Jon Stanley <jonstanley@gmail.com> - 1.0-2
- Remove RHEL conditional for Fedora

* Sun Jun 11 2017 Jon Stanley <jonstanley@gmail.com> - 1.0-1
- Python 3 compatibility (carlgeorge)
- Migrate to argparse
- Various minor cleanups
- Remove BuildRoot tag as no longer needed

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 16 2009 Jon Stanley <jonstanley@gmail.com> - 0.2-1
- Add option for getting keys from a file

* Tue Jul 28 2009 Jon Stanley <jonstanley@gmail.com> - 0.1-3
- Fix spec typo

* Sun Jul 26 2009 Jon Stanley <jonstanley@gmail.com> - 0.1-2
- Review fixup (combine install lines)

* Sun Jul 26 2009 Jon Stanley <jonstanley@gmail.com> - 0.1-1
- Initial package
