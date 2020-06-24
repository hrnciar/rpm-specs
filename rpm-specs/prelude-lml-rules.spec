Name:           prelude-lml-rules
Version:        5.1.0
Release:        2%{?dist}
Summary:        Prelude LML community ruleset
License:        GPLv2+
URL:            https://www.prelude-siem.org/
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Requires:       prelude-lml

%description
Rules for Prelude LML contributed by the community.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/%{name}-check %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/prelude-lml/ruleset
cp -pr ruleset/* %{buildroot}%{_sysconfdir}/prelude-lml/ruleset/

sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{buildroot}%{_bindir}/%{name}-check

%build
# No build action

%check
test -z "`%{buildroot}%{_bindir}/%{name}-check %{buildroot}%{_sysconfdir}/prelude-lml/ruleset/*.rules 2>&1 | grep WARNING`"

%files
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/%{name}-check
%dir %{_sysconfdir}/prelude-lml/ruleset
%dir %{_sysconfdir}/prelude-lml/ruleset/unsupported
%config(noreplace) %{_sysconfdir}/prelude-lml/ruleset/*.rules
%config(noreplace) %{_sysconfdir}/prelude-lml/ruleset/unsupported/*.rules


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.1.0-1
- Bump version 5.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Thomas Andrejak <thomas.andrejak@gmail.com> - 5.0.0-1
- Bump version 5.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.1.0-1
- Bump version 4.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 4.0.0-1
- Bump version 4.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Thomas Andrejak <thomas.andrejak@gmail.com> - 3.1.0-1
- Initial package
