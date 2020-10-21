%{?python_enable_dependency_generator}

%global srcname sphinxcontrib-svg2pdfconverter

Name:           python-%{srcname}
Version:        1.1.0
Release:        2%{?dist}
Summary:        Sphinx SVG to PDF Converter Extension

License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-svg2pdfconverter/
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist Sphinx}
BuildArch:      noarch

%description
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).


%package -n python3-%{srcname}-common
Summary:        Sphinx SVG to PDF Converter Extension - common files

%description -n python3-%{srcname}-common
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains common files.


%package -n python3-sphinxcontrib-inkscapeconverter
Summary:        Sphinx SVG to PDF Converter Extension - Inkscape converter

Requires:       /usr/bin/inkscape
Requires:       python3-%{srcname}-common = %{version}-%{release}

%{?python_provide:%python_provide python3-sphinxcontrib-inkscapeconverter}

%description -n python3-sphinxcontrib-inkscapeconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using Inkscape.


%package -n python3-sphinxcontrib-rsvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - libRSVG converter

Requires:       /usr/bin/rsvg-convert
Requires:       python3-%{srcname}-common = %{version}-%{release}

%{?python_provide:%python_provide python3-sphinxcontrib-rsvgconverter}

%description -n python3-sphinxcontrib-rsvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using libRSVG.


%package -n python3-sphinxcontrib-cairosvgconverter
Summary:        Sphinx SVG to PDF Converter Extension - CairoSVG converter

Requires:       %{py3_dist CairoSVG}
Requires:       python3-%{srcname}-common = %{version}-%{release}

%{?python_provide:%python_provide python3-sphinxcontrib-cairosvgconverter}

%description -n python3-sphinxcontrib-cairosvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using CairoSVG.


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}-common
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/sphinxcontrib_svg2pdfconverter*nspkg.pth
%{python3_sitelib}/sphinxcontrib_svg2pdfconverter-*.egg-info


%files -n python3-sphinxcontrib-inkscapeconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/inkscapeconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/inkscapeconverter.py


%files -n python3-sphinxcontrib-rsvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/rsvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/rsvgconverter.py


%files -n python3-sphinxcontrib-cairosvgconverter
%{python3_sitelib}/sphinxcontrib/__pycache__/cairosvgconverter.*.pyc
%{python3_sitelib}/sphinxcontrib/cairosvgconverter.py


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Julian Sikorski <belegdol@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0
- Add -cairosvgconverter subpackage
- Move BuildRequires to main package section
- Add python3-setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Julian Sikorski <belegdol@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-4
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.0-3
- Correct the dependencies between subpackages

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.0-1
- Initial RPM release
