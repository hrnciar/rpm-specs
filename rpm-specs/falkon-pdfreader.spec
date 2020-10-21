%global gitcommit_full dcb8453c21a4562727215e899dad083637bc30d3
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20200924

%global debug_package %{nil}

Name:           falkon-pdfreader
Version:        0
Release:        0.7.%{date}git%{gitcommit}%{?dist}
Summary:        PDF reader extension for Falkon using pdf.js

License:        GPLv3+ and ASL 2.0
URL:            https://github.com/Tarptaeya/PDFReader
Source0:        %{url}/tarball/%{gitcommit_full}


# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

Requires:       falkon%{?_isa} >= 3.1.0

%description
%{summary}.

%prep
%autosetup -n Tarptaeya-PDFReader-%{gitcommit}
mv pdfreader/pdfjs/LICENSE LICENSE_pdfjs


%build
mkdir %{_target_platform}
pushd %{_target_platform}
    %cmake_kf5 ..
popd


%install
pushd %{_target_platform}
    %cmake_install
popd


%files
%license LICENSE LICENSE_pdfjs
%doc README.md
%{_kf5_qtplugindir}/falkon/qml/pdfreader



%changelog
* Fri Sep 25 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.7.20200924gitdcb8453
- Update to latest git

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200725gita37de6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.4.20200725gita37de6f
- Update to latest git

* Tue Jun 23 2020 Vasiliy Glazov <vascom2@gmail.com> - 0-0.4.20190118giteefc135
- Correct build arches

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190118giteefc135
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190118giteefc135
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar  4 2019 Vasiliy Glazov <vascom2@gmail.com> - 0-0.1.20190118giteefc135
- Initial packaging
