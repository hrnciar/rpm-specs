%global srcname libNeuroML

%global _description \
This package provides Python libNeuroML, for working with neuronal models \
specified in NeuroML 2 (http://neuroml.org/neuromlv2).  NeuroML provides an \
object model for describing neuronal morphologies, ion channels, synapses and \
3D network structure.  Documentation is available at \
http://readthedocs.org/docs/libneuroml/en/latest/


Name:           python-%{srcname}
Version:        0.2.50
Release:        1%{?dist}
Summary:        Python libNeuroML for working with neuronal models specified in NeuroML

License:        BSD
URL:            http://neuroml.org/
Source0:        https://github.com/NeuralEnsemble/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
# These require a mongodb db set up, so we disable them
Patch0:         %{srcname}-0.2.45-disable-mongodb-test.patch

BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist tables}
BuildRequires:  %{py3_dist jsonpickle}
BuildRequires:  %{py3_dist pymongo}
BuildRequires:  %{py3_dist sphinx}
Requires:  %{py3_dist lxml}
Requires:  %{py3_dist numpy}
Requires:  %{py3_dist tables}
Requires:  %{py3_dist jsonpickle}
Requires:  %{py3_dist pymongo}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary:    Documentation for %{srcname}

%description doc
%{_description}

%prep
%autosetup -p 1 -n %{srcname}-%{version}

# remove shebang
sed -i '1d' neuroml/nml/nml.py

# remove egg info
rm -fv %{name}.egg-info

# correct end of line encoding
sed -i 's/\r$//' neuroml/examples/test_files/tmp2.swc

%build
%py3_build

# Make documentation
pushd doc && \
    make html SPHINXBUILD=sphinx-build-3 && \
    rm _build/html/.buildinfo -fv && \
popd || exit -1

%install
%py3_install

%check
nosetests-3

%files -n python3-%{srcname}
%license LICENSE
%doc README.md AUTHORS
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/neuroml

%files doc
%license LICENSE
%doc README.md AUTHORS
%doc neuroml/examples doc/_build/html/

%changelog
* Sun Jun 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.50-1
- Update to 0.2.50

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.47-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.47-1
- Update to 0.2.47
- use github tar since pypi tar does not contain all required files

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-5
- Update to use conditional for spec uniformity

* Fri Oct 26 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-4
- Correct license
- Remove bcond
- Remove hidden buildinfo file
- Correct end of line encoding
- Remove unneeded shebang (https://github.com/NeuralEnsemble/libNeuroML/issues/77)
- Add missing requires

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-3
- Correct doc build
- Temporarily use bcond

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-2
- Correct doc sub package name

* Thu Oct 25 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.45-1
- Initial build
