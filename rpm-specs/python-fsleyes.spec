%global srcname fsleyes

%global desc \
FSLeyes, the FSL image viewer

# PyPi tar does not include tests
# Upstream says the tests, since they use xvfb etc., may not always pass on all
# platforms.
%bcond_with tests


Name:           python-%{srcname}
Version:        0.34.2
Release:        1%{?dist}
Summary:        FSLeyes, the FSL image viewer

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# from requirements-dev.txt
BuildRequires:  graphviz
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wxpython}
BuildRequires:  freeglut-devel
BuildRequires:  xorg-x11-server-Xvfb

Requires:       dcm2niix
Requires:       python3-matplotlib-wx

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

# Add extra requirements for autogenerator
cat requirements-extra.txt >> requirements.txt
cat requirements-notebook.txt >> requirements.txt

# Remove unnecessary upper limit on Pillow:
# https://github.com/pauldmccarthy/fsleyes/issues/7
# sed -i 's/\(Pillow>=3.2.0\),.*/\1/' requirements.txt

# remove unneeded shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;

%build
%py3_build

# Build documentation
%{__python3} setup.py userdoc
%{__python3} setup.py apidoc
# Remove build artefacts
pushd userdoc
    rm -frv html/.buildinfo
    rm -frv html/.doctrees
    mv html userdoc_html
popd

pushd apidoc
    rm -frv html/.buildinfo
    rm -frv html/.doctrees
    mv html apidoc_html
popd


%install
%py3_install

# remove docs installed in the python bits
rm -rfv $RPM_BUILD_ROOT/%{python3_sitelib}/%{srcname}/userdoc


%check
%if %{with tests}
export MPLBACKEND=wxagg
export FSLEYES_TEST_GL=2.1
xvfb-run -s "-screen 0 640x480x24" pytest-3
sleep 5
xvfb-run -s "-screen 0 640x480x24" pytest-3
sleep 5
xvfb-run -s "-screen 0 640x480x24" pytest-3
sleep 5

# test overlay types for GL14 as well
export FSLEYES_TEST_GL=1.4
xvfb-run -s "-screen 0 640x480x24" pytest-3
%endif

%files -n python3-%{srcname}
%license LICENSE COPYRIGHT
%doc README.rst
%{_bindir}/%{srcname}
%{_bindir}/render
%{_bindir}/fsleyes_unfiltered
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE COPYRIGHT
%doc userdoc/userdoc_html apidoc/apidoc_html

%changelog
* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.34.2-1
- Update to latest release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.32.3-3
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.32.3-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.32.3-1
- Update to 0.32.3

* Fri Feb 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.32.2-1
- Update to latest release

* Sun Feb 16 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.32.0-3
- Fix requirements to remove * since autogenerator doesnt like it

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.32.0-1
- Update to 0.32.0

* Mon Oct 28 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.31.2-1
- Update to 0.31.2

* Mon Sep 23 2019 Aniket Pradhan <major AT fedoraproject DOT org> - 0.31.0-1
- Update to 0.31.0

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.30.1-1
- Update to 0.30.1

* Thu Aug 29 2019 Scott Talbert <swt@techie.net> - 0.30.0-5
- Remove sed patches for sip and revert to wx.siplib (#1739469)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.30.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.30.0-2
- Add new bin file

* Fri Jul 5 2019 Luis M. Segundo <blackfile@fedoraproject.org> - 0.30.0-1
- Update to to 0.30.0

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.29.0-1
- Update to 0.29.0

* Thu Apr 18 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.28.3-1
- Update to latest release
- Rely on automatic generator (enable for F<30)

* Wed Apr 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.28.1-1
- Update to 0.28.1

* Sat Feb 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.27.3-1
- Update to latest upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.26.4-3
- Remove unnecessary pillow version limit
- Use wxpython4 and sip correctly from system

* Mon Nov 26 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.26.4-2
- Fix requires
- Enable available requires

* Fri Nov 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.26.4-1
- Initial build
