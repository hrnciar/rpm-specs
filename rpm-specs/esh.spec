Name:           esh
Version:        0.3.0
Release:        2%{?dist}
Summary:        Simple templating engine based on shell

License:        MIT
URL:            https://github.com/jirutka/esh
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{_bindir}/asciidoctor

Requires:       %{_bindir}/awk
Requires:       %{_bindir}/sed

%description
esh (embedded shell) is a templating engine for evaluating shell commands
embedded in arbitrary templates. It’s like ERB (Embedded RuBy) for shell,
intended to be used for templating configuration files.

%prep
%autosetup


%build
%make_build


%install
%make_install prefix=%{_prefix}


%check
make test

%files
%license LICENSE
%doc README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Jakub Jirutka <jakub@jirutka.cz> - 0.3.0-1
- Update to 0.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-1
- Update to 0.1.1, use %%make macros

* Sat Nov 18 2017 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-1
- New package

