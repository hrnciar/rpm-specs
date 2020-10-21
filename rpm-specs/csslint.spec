%global forgeurl https://github.com/CSSLint/csslint
Version:        1.0.5

%forgemeta

Name:           csslint
Release:        2%{?dist}
Summary:        Detecting potential problems in CSS code

License:        MIT
URL:            http://csslint.net/
Source0:        %{forgesource}
Source1:        %{name}.in

BuildArch:      noarch

Requires:       rhino
Provides:       bundled(npm(clone)) = 2.1.0
Provides:       bundled(npm(parserlib)) = 1.1.1


%description
CSSLint is a tool to help point out problems with your CSS code. It does basic
syntax checking as well as applying a set of rules to the code that look for
problematic patterns or signs of inefficiency. The rules are all pluggable, so
you can easily write your own or omit ones you don't want.


%prep
%forgesetup

sed -e 's|@RHINO_JAR@|%{_datadir}/java/js.jar|g' \
    -e 's|@CSSLINT_JS@|%{_datadir}/%{name}/%{name}-rhino.js|g' \
    < %{SOURCE1} \
    > %{name}


%build


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -t %{buildroot}%{_bindir}/ %{name}
install -m 0444 -t %{buildroot}%{_datadir}/%{name}/ dist/%{name}-rhino.js


%files
%doc CHANGELOG README.md
%{_datadir}/%{name}
%{_bindir}/%{name}


%changelog
* Wed Oct  7 2020 Peter Oliver <rpm@mavit.org.uk> - 1.0.5-2
- Document bundled libs.

* Wed Oct  7 2020 Peter Oliver <rpm@mavit.org.uk> - 1.0.5-1
- Update to 1.0.5.
- Tidy up build.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.10.0-1
- Upstream 0.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.9.10-1
- Upstream 0.9.10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.9.8-1
- Upstream 0.9.8

* Sun Jan 08 2012 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.9.2-2
- Fix attr for Koji build

* Sun Jan 08 2012 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.9.2-1
- Upstream 0.9.2

* Fri Dec 23 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.8.5-1
- Upstream 0.8.5

* Fri Nov 18 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 0.8.1-1
- Initial packaging
