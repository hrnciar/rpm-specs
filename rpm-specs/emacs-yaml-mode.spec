%global pkg yaml-mode

Name:	emacs-%{pkg}
Version:	0.0.14
Release:	3%{?dist}
Summary:	Major mode to edit YAML files for emacs

License:	GPLv2+
URL:	https://github.com/yoshiki/yaml-mode
Source0:	https://github.com/yoshiki/%{pkg}/archive/%{version}.tar.gz
Source1:	yaml-mode-init.el
BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}

%description
Major mode to edit YAML files for emacs

%prep
%setup -q -n %{pkg}-%{version}

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/%{pkg}
make install PREFIX=%{_prefix} INSTALLLIBDIR=%{buildroot}%{_emacs_sitelispdir}/%{pkg}

mkdir -p %{buildroot}/%{_emacs_sitestartdir}
install -pm 644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}

%files
%doc README Changes
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Mark McKinstry <mmckinst@fedoraproject.org> - 0.0.14-1
- upgrade to 0.0.14 (RHBZ#1723973)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Mark McKinstry <mmckinst@umich.edu> - 0.0.13-1
- upgrade to 0.0.13 (RHBZ#1392735)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Mark McKinstry <mmckinst@umich.edu> - 0.0.12-2
- own the directory the package creates
- preserve timestamps on files
- use parallel make macro

* Sat Oct  3 2015 Mark McKinstry <mmckinst@umich.edu> - 0.0.12-1
- upgrade to 0.0.12

* Tue Jul 28 2015 Mark McKinstry <mmckinst@umich.edu> - 0.0.11-1
- initial package
