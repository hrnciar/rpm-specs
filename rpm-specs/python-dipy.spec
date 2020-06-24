# No py3 since it depends on nibabel which we only provide for py3
%global srcname dipy

%global desc %{expand: \
DIPY is a python toolbox for analysis of MR diffusion imaging.
DIPY is for research only; please do not use results from DIPY for clinical
decisions.

Current information can always be found from the DIPY website - http://dipy.org}

# Full documentation downloads 100+MB of data, so we'd rather users look at the
# upstream documentation
%bcond_with docs

# Fail because of xvfb related errors
%bcond_with tests

%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Diffusion MRI utilities in python

License:        BSD
URL:            http://nipy.org/dipy/
Source0:        https://github.com/nipy/dipy/archive/%{version}/%{name}-%{version}.tar.gz

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:      python3-devel
BuildRequires:      gcc
BuildRequires:      %{py3_dist setuptools}
BuildRequires:      %{py3_dist pytest}
BuildRequires:      %{py3_dist Cython}
BuildRequires:      %{py3_dist numpy} >= 1.7.1
BuildRequires:      %{py3_dist scipy} >= 0.9
BuildRequires:      %{py3_dist nibabel} >= 3.0
BuildRequires:      %{py3_dist h5py} >= 2.4
BuildRequires:      %{py3_dist matplotlib}
%if %{with tests}
BuildRequires:      %{py3_dist xvfbwrapper}
BuildRequires:      xorg-x11-server-Xvfb
%endif
Requires:           %{py3_dist h5py} >= 2.4
Requires:           %{py3_dist nibabel} >= 2.3
Requires:           %{py3_dist scipy} >= 0.9
Requires:           %{py3_dist numpy} >= 1.7.1

# Required for some modules but not in Fedora yet
# BuildRequires:      %%{py3_dist cvxpy}

Suggests:           %{py3_dist ipython}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package doc
BuildArch:      noarch
Summary:        %{summary}

%description doc
Documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{version}
export TEST_WITH_XVFB=true
# clean it all up (from the Makefile)
find . -name "*.so" -print -delete
find . -name "*.pyd" -print -delete
find . -name "*.c" -print -delete
find . -name "*.html" -print -delete
rm -rf build
rm -rf docs/_build
rm -rf docs/dist
rm -rf dipy/dipy.egg-info

# Correct interpreter for these---used in building docs and so on
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/docgen_cmd.py
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' doc/tools/build_modref_templates.py
find tools/ -name "*.py" -exec sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' '{}' \;

# Other shebangs and permission fixes
for f in "dipy/boots/resampling.py" "dipy/reconst/benchmarks/bench_csd.py" "dipy/reconst/dki.py" "dipy/reconst/dti.py"  "dipy/workflows/mask.py" "dipy/workflows/tracking.py" "dipy/reconst/dki_micro.py"
do
    chmod -x "$f"
    sed -i '/^#!\/usr\/bin\/env python/ d' "$f"
    sed -i '/^#!\/usr\/bin\/python/ d' "$f"
done

%build
export TEST_WITH_XVFB=true
%py3_build

%if %{with docs}
pushd doc
    export PYTHONPATH=../build/
    make SPHINXBUILD=sphinx-build-3 PYTHON=%{__python3} html
    rm -rf _build/html/.doctrees
    rm -rf _build/html/.buildinfo
popd
%endif

%install
%py3_install

%check
export TEST_WITH_XVFB=True
%if %{with tests}
%{__python3} -c 'import dipy; dipy.test()'
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst Changelog AUTHOR
%{_bindir}/dipy_align_affine
%{_bindir}/dipy_align_syn
%{_bindir}/dipy_apply_transform
%{_bindir}/dipy_ba
%{_bindir}/dipy_denoise_lpca
%{_bindir}/dipy_denoise_mppca
%{_bindir}/dipy_denoise_nlmeans
%{_bindir}/dipy_fetch
%{_bindir}/dipy_fit_csa
%{_bindir}/dipy_fit_csd
%{_bindir}/dipy_fit_dki
%{_bindir}/dipy_fit_dti
%{_bindir}/dipy_fit_ivim
%{_bindir}/dipy_fit_mapmri
%{_bindir}/dipy_gibbs_ringing
%{_bindir}/dipy_horizon
%{_bindir}/dipy_info
%{_bindir}/dipy_labelsbundles
%{_bindir}/dipy_lmm
%{_bindir}/dipy_mask
%{_bindir}/dipy_median_otsu
%{_bindir}/dipy_recobundles
%{_bindir}/dipy_reslice
%{_bindir}/dipy_slr
%{_bindir}/dipy_snr_in_cc
%{_bindir}/dipy_track_local
%{_bindir}/dipy_track_pft
%{_bindir}/dipy_split
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py3.?.egg-info

%files doc
%license LICENSE
# Installed by package
%{_docdir}/%{srcname}/examples
%if %{with docs}
%doc doc/_build/html
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Sat Feb 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.1-1
- Update to new version
- Bump nibabel requirement version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.0.0-1
- update to 1.0.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.16.0-1
- Update to latest upstream release
- Use gittag instead of snapshot
- Add new binaries

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-0.5.git756b519
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.0-0.4.git756b519
- Provide Requires explictly as they are not picked up by the autogenerator

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.0-0.3.git756b519
- remove python3-vtk dep
- not available in F29 currently, and only needed for doc generation which is disabled

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.0-0.2.git756b519
- Disable doc generation

* Thu Nov 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.15.0-0.1.git756b519
- Initial rpm build
