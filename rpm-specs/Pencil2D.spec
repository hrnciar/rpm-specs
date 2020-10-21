%define nameapp pencil2d

Name:           Pencil2D
Version:        0.6.5
Release:        1%{?dist}
Summary:        Animation/drawing software
License:        GPLv2
URL:            https://gitlab.com/chchwy/%{nameapp}
Source0:        %{url}/-/archive/v%{version}/pencil-%{version}.tar.gz

BuildRequires:  qt5-devel
BuildRequires:	desktop-file-utils
Requires:       hicolor-icon-theme

%description
Pencil2D lets you create traditional hand-drawn animation

%prep
%autosetup -n %{nameapp}-v%{version}

%build
%{qmake_qt5} PREFIX=%{_prefix}
make %{?_smp_mflags}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%install
export INSTALL_ROOT=%{buildroot}
%make_install

%files
%license LICENSE.TXT
%doc docs/*
%{_bindir}/%{nameapp}
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/%{nameapp}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{nameapp}.*
%{_datadir}/zsh/site-functions/_%{nameapp}


%changelog
* Wed Aug 26 2020 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Marie Loise Nolden <loise@kde.org> - 0.6.4-4	
- Fix for Qt 5.15.0 

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4

* Thu Mar 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.3-2
- Fix comment #17 BZ #1632851 and #1691144

* Sun Mar 17 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Luis M. Segundo <blackfile@fedoraproject.org> - 0.6.2-1
- first release
