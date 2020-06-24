%global modname cairosvg
%global srcname CairoSVG
%global py3_prefix python%{python3_pkgversion}

Name:               python-cairosvg
Version:            2.4.2
Release:            4%{?dist}
Summary:            A Simple SVG Converter for Cairo

License:            LGPLv3+
URL:                https://cairosvg.org/
Source0:            %pypi_source
Patch0:             %{name}-disable-flake8-isort.patch

BuildArch:          noarch

BuildRequires:      %{py3_prefix}-devel
BuildRequires:      %{py3_prefix}-cairocffi
BuildRequires:      %{py3_prefix}-cssselect2
BuildRequires:      %{py3_prefix}-defusedxml
BuildRequires:      %{py3_prefix}-pillow
BuildRequires:      %{py3_prefix}-setuptools
BuildRequires:      %{py3_prefix}-pytest
BuildRequires:      %{py3_prefix}-pytest-cov
BuildRequires:      %{py3_prefix}-pytest-runner
# actually python3-cairocffi should have that dependency (see bug 1698217) but
# for now just add the requirement here.
BuildRequires:      %{py3_prefix}-xcffib


%description
CairoSVG is a SVG 1.1 to PNG, PDF, PS and SVG converter which can also be used
as a Python library.

%package -n python3-cairosvg
Summary:            A Simple SVG Converter for Cairo

# The subpackage used to be called this on accident.
# https://bugzilla.redhat.com/show_bug.cgi?id=1263793
Provides:           python3-CairoSVG

# %%{_bindir}/cairosvg was moved from here
Conflicts:          python2-cairosvg < 1.0.20-11

# actually python3-cairocffi should have that dependency (see bug 1698217) but
# for now just add the requirement here.
Requires:           %{py3_prefix}-xcffib

%description -n python3-cairosvg
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info in case it exists
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v
# remove file which is only required for unit tests
rm -f %{buildroot}%{python3_sitelib}/%{modname}/test_api.py


%files -n python3-cairosvg
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{srcname}-%{version}-*
%{_bindir}/cairosvg

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 2.4.2-2
- add missing sources

* Sun Nov 03 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 2.4.2-1
- new upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.20-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.20-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.20-11
- Subpackage python2-cairosvg has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.20-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.20-6
- Python 2 binary package renamed to python2-cairosvg
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.20-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Ralph Bean <rbean@redhat.com> - 1.0.20-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 31 2015 Ralph Bean <rbean@redhat.com> - 1.0.19-1
- new version

* Wed Oct 21 2015 Ralph Bean <rbean@redhat.com> - 1.0.18-1
- new version

* Sat Oct 10 2015 Ralph Bean <rbean@redhat.com> - 1.0.17-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 1.0.16-2
- Rename the python3 subpackage and Provide the old name.

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 1.0.16-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Ralph Bean <rbean@redhat.com> - 1.0.13-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 1.0.9-1
- Latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 08 2014 Ralph Bean <rbean@redhat.com> - 1.0.7-1
- Latest upstream.

* Fri Mar 07 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-1
- Latest upstream.

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 1.0.4-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Ralph Bean <rbean@redhat.com> - 0.5-2
- Updated license to LGPLv3+ after clarification from upstream.
  https://github.com/Kozea/CairoSVG/pull/8
- Removed reStructuredText markup from the description.

* Sat Apr 13 2013 Ralph Bean <rbean@redhat.com> - 0.5-1
- Initial package for Fedora
