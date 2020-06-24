Name:           rfcdiff
Version:        1.47
Release:        4%{?dist}
Summary:        Compares two internet draft files and outputs the difference

License:        GPLv2+
URL:            http://tools.ietf.org/tools/rfcdiff/
Source0:        http://tools.ietf.org/tools/rfcdiff/%{name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  txt2man

%description
The purpose of this program is to compare two versions of an
internet-draft, and as output produce a diff in one of several
formats:
- side-by-side html diff
- paged wdiff output in a text terminal
- a text file with changebars in the left margin
- a simple unified diff output

In all cases, internet-draft headers and footers are stripped before
generating the diff, to produce a cleaner diff.


%prep
%setup -q
sed -i 's|include ../Makefile.common|include Makefile.common|g' Makefile

%build
make manpage


%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1

install -pm 0755 %{name} %{buildroot}%{_bindir}/
install -pm 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/


%files
%doc changelog copyright todo
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.47-1
- Update to 1.47.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 28 2016 Richard Shaw <hobbes1069@gmail.com> - 1.45-1
- Update to latest upstream release.

* Thu Mar 24 2016 Richard Shaw <hobbes1069@gmail.com> - 1.44-1
- Update to latest upstream release.

* Wed Mar  2 2016 Richard Shaw <hobbes1069@gmail.com> - 1.43-1
- Update to latest upstream release.

* Thu Feb 18 2016 Richard Shaw <hobbes1069@gmail.com> - 1.42-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 14 2012 Richard Shaw <hobbes1069@gmail.com> - 1.41-2
- Add missing BuildRequires.

* Mon Feb 06 2012 Richard Shaw <hobbes1069@gmail.com> - 1.41-1
- Initial release.
