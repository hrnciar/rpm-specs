Name:           ternimal
Version:        0.1.0
Release:        6%{?dist}
Summary:        Simulate a lifeform in the terminal

License:        GPLv3+
URL:            https://github.com/p-e-w/ternimal
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%prep
%autosetup -p1

%build
%{__rustc} %{__global_rustflags} ternimal.rs -o ternimal

%install
%{__install} -Dpm0755 -t %{buildroot}%{_bindir} ternimal

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/ternimal

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Update to 0.1.0

* Thu Nov 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-1.20171109.git.2eea4f4
- Initial package
