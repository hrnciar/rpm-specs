# These are unreliable, unfortunately.
%bcond_with xvfb_tests

%global srcname fsleyes-widgets

%global desc \
A collection of custom wx widgets and utilities used by FSLeyes.


Name:           python-%{srcname}
Version:        0.9.0
Release:        3%{?dist}
Summary:        A collection of custom wx widgets and utilities used by FSLeyes

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist deprecation}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist wxpython}
BuildRequires:  xorg-x11-server-Xvfb

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:  %{py3_dist six}
Requires:  %{py3_dist deprecation}
Requires:  %{py3_dist numpy}
Requires:  %{py3_dist matplotlib}
Requires:  %{py3_dist wxpython}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package doc
Summary:        %{summary}

%description doc
This package contains documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}
rm -rfv fsleyes_widgets.egg-info

# remove unneeded shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;


%build
%py3_build

# Build documentation
PYTHONPATH=.  sphinx-build-3 doc html
# Remove build artefacts
rm -frv html/.buildinfo
rm -frv html/.doctrees


%install
%py3_install


%check
%if %{with xvfb_tests}
# From https://git.fmrib.ox.ac.uk/fsl/fsleyes/widgets/blob/master/.ci/test_template.sh
# These tests fail, so I've disabled them for the time being. Upstream has been e-mailed.
# set sceen size for test_widgetgrid.py
xvfb-run -a -s "-screen 0 1920x1200x24" pytest-3 tests --ignore=tests/test_autotextctrl.py --ignore=tests/test_bitmapradio.py --ignore=tests/test_bitmaptoggle.py --ignore=tests/test_colourbutton.py --ignore=tests/test_floatslider.py --ignore=tests/test_notebook.py --ignore=tests/test_rangeslider.py --ignore=tests/test_texttag.py --ignore=tests/test_numberdialog.py
%endif

%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst
%{python3_sitelib}/fsleyes_widgets/
%{python3_sitelib}/fsleyes_widgets-%{version}-py3.?.egg-info

%files doc
%license LICENSE COPYRIGHT
%doc html

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.0-2
- Explicitly BR setuptools

* Sun Jun 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.0-1
- Update to new release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.4-1
- Update to 0.8.4
- Make tests conditional

* Mon Sep 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.2-1
- Update to 0.8.2

* Wed Sep 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-2
- Fix failing tests
- https://github.com/pauldmccarthy/fsleyes-widgets/issues/2

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update to 0.8.0
- Report and disable failing test

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Petr Viktorin <pviktori@redhat.com> - 0.7.3-2
- Require sphinx_rtd_theme, which is no longer provided in Sphinx 2.0+

* Sat Feb 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.3-1
- Update to latest release
- Remove py2 conditionals

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.0-3
- Fix doc building on F29-

* Thu Nov 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.0-2
- Remove leftover files from the doc
- Move requires to py3 sub package
- Remove dot at end of summary

* Fri Nov 02 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.7.0-1
- Initial build
