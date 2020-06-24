Name:           translate-shell
Version:        0.9.6.12
Release:        1%{?dist}
Summary:        A command-line online translator

License:        Public Domain
URL:            https://github.com/soimort/translate-shell
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       gawk
Requires:       curl
Requires:       rlwrap
Requires:       fribidi

BuildArch:      noarch

%description
Translate Shell (formerly Google Translate CLI) is a command-line
translator powered by Google Translate (default), Bing Translator,
Yandex.Translate and Apertium.

%prep
%autosetup
#https://github.com/soimort/translate-shell/issues/180
sed -i 's|install: build|install:|' Makefile


%build
%make_build
sed -i 's|/usr/bin/env bash|/usr/bin/bash|' build/trans

%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc CONTRIBUTING.md README.md WAIVER
%{_bindir}/trans
%{_mandir}/man1/trans.1*



%changelog
* Mon May 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.12-1
- Update to 0.9.6.12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 26 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.11-1
- Update to 0.9.6.11

* Tue Apr 23 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.10-1
- Update to 0.9.6.10

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.9-1
- Update to 0.9.6.9

* Tue Aug 14 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.8-1
- Update to 0.9.6.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.7-1
- Update to 0.9.6.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.6-1
- Update to 0.9.6.6

* Mon Oct 16 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.5-1
- Update to 0.9.6.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-3
- Clean spec to pass review

* Fri Jun 02 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-2
- Clean spec

* Thu Jun 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-1
- Update to 0.9.6.4

* Wed May 31 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.3-1
- Initial packaging
