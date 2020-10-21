%global pypi_name trimesh

Name:           python-%{pypi_name}
Version:        3.8.10
Release:        1%{?dist}
Summary:        Import, export, process, analyze and view triangular meshes

License:        MIT
URL:            https://trimsh.org

Source0:        https://github.com/mikedh/trimesh/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(msgpack-python)
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rtree)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(shapely)
BuildRequires:  python3dist(svg.path)
BuildRequires:  python3dist(sympy)

# blender is expensive, so we make it opt in
%bcond_with blender_tests
%if %{with blender_tests}
BuildRequires:  blender
%endif

# https://github.com/cnr-isti-vclab/meshlab/issues/237
#BuildRequires:  /usr/bin/xvfb-run
#BuildRequires:  /usr/bin/meshlabserver

%?python_enable_dependency_generator

%description
Trimesh is a pure Python library for loading and using triangular meshes with
an emphasis on watertight meshes. The goal of the library is to provide
a fully featured and well tested Trimesh object which allows for easy
manipulation and analysis, in the style of the Polygon object in the Shapely
library.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Recommends:     python3-%{pypi_name}-easy = %{version}-%{release}
Suggests:       python3-%{pypi_name}-all = %{version}-%{release}

# for trimesh.boolean
Recommends:     openscad
Recommends:     blender

%description -n python3-%{pypi_name}
Trimesh is a pure Python library for loading and using triangular meshes with
an emphasis on watertight meshes. The goal of the library is to provide
a fully featured and well tested Trimesh object which allows for easy
manipulation and analysis, in the style of the Polygon object in the Shapely
library.


%package -n     python3-%{pypi_name}-easy
Summary:        Easy dependencies for %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}-easy}

Requires:       python3-%{pypi_name} = %{version}-%{release}

Requires:       python3dist(lxml)
Requires:       python3dist(pyglet)
Requires:       python3dist(shapely)
Requires:       python3dist(rtree)
Requires:       python3dist(svg.path)
Requires:       python3dist(sympy)
Requires:       python3dist(msgpack)
Requires:       python3dist(pillow)
Requires:       python3dist(requests)
Requires:       python3dist(colorlog)

# not yet packaged, cannot recommend
#Requires:      python3dist(xxhash)

%description -n python3-%{pypi_name}-easy
Extra dependencies for trimesh[easy].


%package -n     python3-%{pypi_name}-all
Summary:        All dependencies for %{pypi_name}
%{?python_provide:%python_provide python3-%{pypi_name}-all}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-%{pypi_name}-easy = %{version}-%{release}

Requires:       python3dist(setuptools)

# not yet packaged, cannot recommend
#Requires:      python3dist(python-fcl)

# triangle has nonfree dependencies
#Never:         python3dist(triangle)

%description -n python3-%{pypi_name}-all
Extra dependencies for trimesh[all].


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%check
# test_export doesn't work in mock:
# https://github.com/cnr-isti-vclab/meshlab/issues/237
# fail if we get a 32 bit builder: test_load_save_invariance, test_svg, test_composite, test_dense, test_flat, test_flipped, test_reshape, test_transpose, test_brle_encode_decode, test_brle_length, test_brle_logical_not, test_brle_to_dense, test_brle_to_rle, test_rle_encode_decode
# https://github.com/mikedh/trimesh/issues/690#issuecomment-577371622
%{__python3} -m pytest -v \
%if %{with blender_tests}
-k "not test_export and not test_layer and not test_load_save_invariance and not test_svg and not test_composite and not test_dense and not test_flat and not test_flipped and not test_reshape and not test_transpose and not test_brle_encode_decode and not test_brle_length and not test_brle_logical_not and not test_brle_to_dense and not test_brle_to_rle and not test_rle_encode_decode"
%else
-k "not test_export and not test_layer and not test_dae and not (LightTests and test_scene) and not test_load_save_invariance and not test_svg and not test_composite and not test_dense and not test_flat and not test_flipped and not test_reshape and not test_transpose and not test_brle_encode_decode and not test_brle_length and not test_brle_logical_not and not test_brle_to_dense and not test_brle_to_rle and not test_rle_encode_decode"
%endif


%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python3-%{pypi_name}-easy
# empty

%files -n python3-%{pypi_name}-all
# empty


%changelog
* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.8.10-1
- Update to latest release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.34-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.6.34-1
- Update to latest release

* Fri Feb 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.5.23-2
- Temporarily disable tests that fail on 32 bit builders
- https://github.com/mikedh/trimesh/issues/690

* Fri Feb 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.5.23-1
- Update to latest release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.37.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 2.37.12-5
- Drop weak dependencies on packages not available in Fedora

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.37.12-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.37.12-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.37.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Miro Hrončok <mhroncok@redhat.com> - 2.37.12-1
- Update to 2.37.12 (#1678964)

* Mon Feb 18 2019 Lumír Balhar <lbalhar@redhat.com> - 2.36.29-1
- Update to 2.36.29 (#1678054)

* Sat Feb 16 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.36.28-1
- Update to 2.36.28 (#1677725)

* Sun Feb 10 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.36.24-1
- Update to 2.36.24 (#1668080)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.36.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.36.13-1
- Update to 2.36.13 (#1667470)

* Fri Nov 09 2018 Miro Hrončok <mhroncok@redhat.com> - 2.35.24-1
- Update to 2.35.24 (#1648477)

* Mon Sep 03 2018 Miro Hrončok <mhroncok@redhat.com> - 2.33.12-1
- Update to 2.33.12

* Mon Sep 03 2018 Miro Hrončok <mhroncok@redhat.com> - 2.33.11-1
- Initial package
