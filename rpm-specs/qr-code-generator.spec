%global richname QR-Code-generator

Name: qr-code-generator
Version: 1.6.0
Release: 2%{?dist}

License: MIT
Summary: High-quality QR Code generator library
URL: https://github.com/nayuki/%{richname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/nayuki/QR-Code-generator/pull/72
Patch100: %{name}-build-fixes.patch

BuildRequires: python3-devel
BuildRequires: gcc-c++
BuildRequires: gcc

%description
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen
Summary: High-quality QR Code generator library (plain C version)

%description -n libqrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen-devel
Summary: Development files for libqrcodegen
Requires: libqrcodegen%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegen-devel
Development files and headers for high-quality QR Code generator library
(plain C version).

%package -n libqrcodegencpp
Summary: High-quality QR Code generator library (C++ version)

%description -n libqrcodegencpp
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegencpp-devel
Summary: Development files for libqrcodegencpp
Requires: libqrcodegencpp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegencpp-devel
Development files and headers for high-quality QR Code generator library
(C++ version).

%package -n python3-qrcodegen
Summary: High-quality QR Code generator library (Python version)
BuildArch: noarch
%{?python_provide:%python_provide python3-qrcodegen}

%description -n python3-qrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%prep
%autosetup -n %{richname}-%{version} -p1

%build
# Exporting correct build flags...
%set_build_flags

# Building plain C version...
pushd c
%make_build
popd

# Building C++ version...
pushd cpp
%make_build
popd

# Building Python version...
pushd python
%py3_build
popd

%install
# Installing plain C version...
pushd c
%make_install LIBDIR=%{buildroot}%{_libdir} INCLUDEDIR=%{buildroot}%{_includedir}/qrcodegen
popd

# Installing C++ version...
pushd cpp
%make_install LIBDIR=%{buildroot}%{_libdir} INCLUDEDIR=%{buildroot}%{_includedir}/qrcodegencpp
popd

# Installing Python version...
pushd python
%py3_install
popd

%files -n libqrcodegen
%license Readme.markdown
%{_libdir}/libqrcodegen.so.1*

%files -n libqrcodegen-devel
%{_includedir}/qrcodegen/
%{_libdir}/libqrcodegen.so

%files -n libqrcodegencpp
%license Readme.markdown
%{_libdir}/libqrcodegencpp.so.1*

%files -n libqrcodegencpp-devel
%{_includedir}/qrcodegencpp/
%{_libdir}/libqrcodegencpp.so

%files -n python3-qrcodegen
%license Readme.markdown
%{python3_sitelib}/qrcodegen.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/qrcodegen-*.egg-info/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.0-1
- Updated to version 1.6.0.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3.20191014git67c6246
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2.20191014git67c6246
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1.20191014git67c6246
- Initial SPEC release.
