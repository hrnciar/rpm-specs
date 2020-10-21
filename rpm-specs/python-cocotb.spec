# NOTE: the only library that we can't build in Fedora
# is the FLI interface to modelsim. See:
# https://github.com/cocotb/cocotb/blob/master/cocotb_build_libs.py#L339
# One way to work around that would be to ship the cocotb_build_libs.py
# script and install it system-wide. I have't decided if that makes sense.
# But I believe that this package will actually still work with modelsim
# through VPI; so ultimately I don't think there's a huge reduction in
# functionality. Still, I wanted to write this down somewhere.

# Created by pyp2rpm-3.3.2
%global pypi_name cocotb

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        3%{?dist}
Summary:        Coroutine Co-simulation Test Bench

License:        BSD
URL:            https://github.com/cocotb/cocotb
Source0:        https://github.com/cocotb/cocotb/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  gcc, gcc-c++, make

# iverilog and ghdl are the FOSS simulators. cocotb supports both.
# We need them to run the tests... although the main one we need
# is iverilog. ghdl is apparently not currently built on armv7hl.
%ifnarch armv7hl
BuildRequires:  ghdl
%endif
BuildRequires:  iverilog

# Test failure on s390x with iverilog-- needs more investigation,
# will disable build for now.
# See https://github.com/cocotb/cocotb/issues/2044
ExcludeArch:    s390x

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Provide "cocotb", as that's the upstream name and this is
# a framework end-users would use directly.
Provides:       cocotb = %{version}-%{release}

# It isn't *strictly* necessary to have iverilog/ghdl installed, especially
# since cocotb also supports non-FOSS simulators. Thus, use a weak dep to
# pull them in (but allow someone to remove them if necessary).
Recommends:     iverilog, ghdl

%description
cocotb is a coroutine based cosimulation library for writing VHDL
and Verilog testbenches in Python.

%description -n python3-%{pypi_name}
cocotb is a coroutine based cosimulation library for writing VHDL
and Verilog testbenches in Python.

%prep
%autosetup -n %{pypi_name}-%{version}

# Only run the tests, not the examples.
# Examples require /usr/bin/cocotb-config already installed.
sed "/\$(MAKE) -k -C examples/d" -i Makefile

# Fix the 'combine_results.py' script to use python3.
sed 's/env python/python3/g' -i bin/combine_results.py

# Should remove chbangs from non-script library files.
sed "/env python/d" -i cocotb/*.py
sed "/env python/d" -i cocotb/drivers/*.py
sed "/env python/d" -i cocotb/generators/*.py
sed "/env python/d" -i cocotb/monitors/*.py

%build
%py3_build

%install
%py3_install

%check
# Run tests with the FOSS simulators.
# To do this, we need cocotb-config to be on the path.
export PYTHON_BIN=python3
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
# Run tests with iverilog on all supported architectures.
make SIM=icarus

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/cocotb-config
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py*.*.egg-info

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.4.0-1
- Update to latest upstream release.
- Package is now arched; simulator libraries compiled at install time.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.1-1
- Update to latest upstream release.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.3.0-1
- Update to latest upstream release.

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-3
- Move Recommends on iverilog/ghdl into python3 subpackage.

* Tue Sep 24 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-2
- Rename package to 'python-cocotb', provide 'cocotb'.
- Remove unnecessary manual dependency on setuptools.
- Remove unnecessary removal of egg info file.
- Change combine_results script to not use "env" to find python3 interpreter
- Change egg info file in files list to use '*' instead of '?' pattern matching.

* Fri Jul 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2.0-1
- Initial package.
