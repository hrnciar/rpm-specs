# pipenv rebase checklist
# - Update version, release tag, add changelog
# - Update the test_artifacts_commit macro to point to the correct commit
# - Uplead both new sources to the side cache
# - Update the `bundled-licenses` file (see guidance inside)
# - Update licenses in %%files section (see guidance in that section)
# - Update versions of bundled packages, and build/required versions of
#   unbundled packages (see files pipenv/vendor/vendor.txt
#   pipenv/vendor/vendor_pip.txt inside the sources, and possibly diff them
#   with the previous version)

%global base_version        2020.8.13
# %%global prerelease_version  --

# Test artifacts are not released, we have to download the commit tree
# Upstream issue: https://github.com/pypa/pipenv/issues/4237
# To update: go to GitHub, find to what commit the submodule `tests/pypi`
#   pointed at the time of the release of pipenv
%global test_artifacts_commit 1881ecb45431952d2e18e2be3416a8835e53778a

%global upstream_version %{base_version}%{?prerelease_version}

Name:           pipenv
Version:        %{base_version}%{?prerelease_version:~%{prerelease_version}}
Release:        1%{?dist}
Summary:        The higher level Python packaging tool

# Pipenv source code is MIT, there are bundled packages having different licenses
# - See file `bundled-licenses`

License:        MIT and BSD and ASL 2.0 and LGPLv2+ and Python and ISC and MPLv2.0 and (ASL 2.0 or BSD) and CC-BY-SA and Unlicense
URL:            https://github.com/pypa/pipenv
Source0:        https://github.com/pypa/%{name}/archive/v%{upstream_version}/%{name}-%{upstream_version}.tar.gz

Source1:        https://github.com/sarugaku/pipenv-test-artifacts/archive/%{test_artifacts_commit}/pipenv-test-artifacts-%{test_artifacts_commit}.tar.gz

# List of licenses of the bundled packages
Source2:        bundled-licenses

# Adds "pytest_pypi.plugin import pypi, ..." to conftest,
# as we don't have that plugin installed and it is not autodiscovered
Patch2:         0002-import-pytest-pypi.patch

# Use the system level root certificate instead of the one bundled in certifi
# https://bugzilla.redhat.com/show_bug.cgi?id=1655253
Patch4:         dummy-certifi.patch

BuildArch:      noarch

BuildRequires:  ca-certificates
# gcc is only needed for tests, this is a noarch package
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(parver)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-click)
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(virtualenv-clone)

# Optional condition that makes "python" mean Python 2
# Useful to tests if pipenv can manage python 2 venvs, but unnecessary dep
%bcond_with python2_tests

%if %{with python2_tests}
BuildRequires:  python2-devel
%endif

# Packages vendored upstream
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(attrs) >= 1.3
BuildRequires:  python3dist(cached-property) >= 1.5.1
# Bundled version of cerberus is 1.3.2, but Fedora has an older version
BuildRequires:  python3dist(cerberus) >= 1.2
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(click) >= 7.1.2
BuildRequires:  python3dist(colorama) >= 0.4.3
BuildRequires:  python3dist(distlib) >= 0.3
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(first) >= 2.0.1
BuildRequires:  python3dist(chardet) >= 3.0.4
BuildRequires:  python3dist(iso8601) >= 0.1.12
BuildRequires:  python3dist(jinja2) >= 2.11.2
BuildRequires:  python3dist(markupsafe) >= 1.1.1
BuildRequires:  python3dist(packaging) >= 20.3
# Bundled version of parse is 1.15, but Fedora has an older version
BuildRequires:  python3dist(parse) >= 1.8.4
BuildRequires:  python3dist(pexpect) >= 4.8
BuildRequires:  python3dist(ptyprocess) >= 0.6
BuildRequires:  python3dist(pyparsing) >= 2.4.7
BuildRequires:  python3dist(python-dotenv) >= 0.10.3
BuildRequires:  python3dist(requests) >= 2.20
# Bundled version of semver is 2.9, but Fedora has an older version
BuildRequires:  python3dist(semver) >= 2.8.1
# Bundled version of shellingham is 1.3.2, but Fedora has an older version
BuildRequires:  python3dist(shellingham) >= 1.2.7
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(toml) >= 0.10.1
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(yarg) >= 0.1.9
BuildRequires:  python3dist(pipdeptree)
BuildRequires:  python3dist(pipreqs)
# Bundled version of plette is 0.2.3, but Fedora has an older version
BuildRequires:  python3dist(plette) >= 0.2.2

%{?python_provide:%python_provide python3-%{name}}

Requires:       ca-certificates
Requires:       which

Requires:       python3dist(virtualenv-clone)
Requires:       python3dist(virtualenv)

# Packages vendored upstream
Requires:       python3dist(appdirs)
Requires:       python3dist(attrs) >= 1.3
Requires:       python3dist(cached-property) >= 1.5.1
# Bundled version of cerberus is 1.3.2, but Fedora has an older version
Requires:       python3dist(cerberus) >= 1.2
Requires:       python3dist(certifi)
Requires:       python3dist(click) >= 7.1.2
Requires:       python3dist(colorama) >= 0.4.3
Requires:       python3dist(distlib) >= 0.3
Requires:       python3dist(docopt) >= 0.6.2
Requires:       python3dist(first) >= 2.0.1
Requires:       python3dist(chardet) >= 3.0.4
Requires:       python3dist(iso8601) >= 0.1.12
Requires:       python3dist(jinja2) >= 2.11.2
Requires:       python3dist(markupsafe) >= 1.1.1
Requires:       python3dist(packaging) >= 20.3
# Bundled version of parse is 1.15, but Fedora has an older version
Requires:       python3dist(parse) >= 1.8.4
Requires:       python3dist(pexpect) >= 4.8
Requires:       python3dist(ptyprocess) >= 0.6
Requires:       python3dist(pyparsing) >= 2.4.7
Requires:       python3dist(python-dotenv) >= 0.10.3
Requires:       python3dist(requests) >= 2.20
# Bundled version of semver is 2.9, but Fedora has an older version
Requires:       python3dist(semver) >= 2.8.1
# Bundled version of shellingham is 1.3.2, but Fedora has an older version
Requires:       python3dist(shellingham) >= 1.2.7
Requires:       python3dist(six)
Requires:       python3dist(toml) >= 0.10.1
Requires:       python3dist(urllib3)
Requires:       python3dist(yarg) >= 0.1.9
Requires:       python3dist(pipdeptree)
Requires:       python3dist(pipreqs)
# Bundled version of plette is 0.2.3, but Fedora has an older version
Requires:       python3dist(plette) >= 0.2.2

# Following packages bundled under vendor directory are not
# packaged for Fedora yet.
# TODO package for Fedora and unbundle
Provides:       bundled(python3dist(click-didyoumean)) == 0.0.3
Provides:       bundled(python3dist(delegator.py)) == 0.1.1
# Needs requirementslib (see below)
Provides:       bundled(python3dist(passa))
# This library uses pip.internals. Some changes in init methods happened there.
# So version 1.3.3 is useless with pip 19+ and newer versions will break pipenv
# because pipenv has bundled patched pip.
Provides:       bundled(python3dist(requirementslib)) == 1.5.13
# Dependency of passa
Provides:       bundled(python3dist(resolvelib)) == 0.3.0

# The sources contains patched versions of following packages:
Provides:       bundled(python3dist(crayons)) == 0.1.2
Provides:       bundled(python3dist(pipfile)) == 0.0.2
Provides:       bundled(python3dist(pip-tools)) == 5.0.0
Provides:       bundled(python3dist(pip)) == 20.0.2
Provides:       bundled(python3dist(safety)) == 1.8.7

# We cannot unbundle this easily,
# See https://bugzilla.redhat.com/show_bug.cgi?id=1767003
Provides:       bundled(python3dist(backports.functools_lru_cache)) == 1.6.1
Provides:       bundled(python3dist(backports.shutil_get_terminal_size)) == 1.0.0
Provides:       bundled(python3dist(click-completion)) == 0.5.2
Provides:       bundled(python3dist(enum34)) == 1.1.10
Provides:       bundled(python3dist(pathlib2)) == 2.3.5
Provides:       bundled(python3dist(scandir)) == 1.10
Provides:       bundled(python3dist(tomlkit)) == 0.5.11

# The packages bundled with pip (20.0.2):
Provides:       bundled(python3dist(CacheControl)) = 0.12.5
Provides:       bundled(python3dist(appdirs)) = 1.4.3
Provides:       bundled(python3dist(certifi)) = 2019.9.11
Provides:       bundled(python3dist(chardet)) = 3.0.4
Provides:       bundled(python3dist(colorama)) = 0.4.1
Provides:       bundled(python3dist(contextlib2)) = 0.6.0
Provides:       bundled(python3dist(distlib)) = 0.2.9.post0
Provides:       bundled(python3dist(distro)) = 1.4.0
Provides:       bundled(python3dist(html5lib)) = 1.0.1
Provides:       bundled(python3dist(idna)) = 2.8
Provides:       bundled(python3dist(msgpack-python)) = 0.6.2
Provides:       bundled(python3dist(packaging)) = 19.2
Provides:       bundled(python3dist(pep517)) = 0.7.0
Provides:       bundled(python3dist(progress)) = 1.5
Provides:       bundled(python3dist(pyparsing)) = 2.4.2
Provides:       bundled(python3dist(pytoml)) = 0.1.21
Provides:       bundled(python3dist(requests)) = 2.22.0
Provides:       bundled(python3dist(retrying)) = 1.3.3
Provides:       bundled(python3dist(setuptools)) = 41.4.0
Provides:       bundled(python3dist(six)) = 1.12.0
Provides:       bundled(python3dist(urllib3)) = 1.25.6
Provides:       bundled(python3dist(webencodings)) = 0.5.1

# Re-bundled because it's only used by pipenv
Provides:       bundled(python3dist(pip-shims)) = 0.5.3
Provides:       bundled(python3dist(pythonfinder)) = 1.2.4
Provides:       bundled(python3dist(yaspin)) = 0.15.0
Provides:       bundled(python3dist(vistir)) = 0.5.2

# Newly discovered bundled libraries - consider unbundling
Provides:       bundled(python3dist(more-itertools)) = 5.0.0
Provides:       bundled(python3dist(funcsigs)) = 1.0.2
Provides:       bundled(python3dist(importlib-resources)) = 1.5.0
Provides:       bundled(python3dist(contextlib2)) = 0.6.0.post1
Provides:       bundled(python3dist(importlib_metadata)) = 1.6.0
Provides:       bundled(python3dist(pep517)) = 0.8.2
Provides:       bundled(python3dist(zipp)) = 0.6.0
Provides:       bundled(python3dist(pep514tools)) = 0.1.0
Provides:       bundled(python3dist(orderedmultidict)) = 1.0.1
Provides:       bundled(python3dist(dparse)) = 0.5.0
Provides:       bundled(python3dist(pyyaml)) = 5.3.1
Provides:       bundled(python3dist(dateutil)) = 2.8.1

%description
The officially recommended Python packaging tool that aims to bring
the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.)
to the Python world. It automatically creates and manages a virtualenv for
your projects, as well as adds/removes packages from your Pipfile as you
install/uninstall packages. It also generates the ever–important Pipfile.lock,
which is used to produce deterministic builds.

%package -n %{name}-doc
Summary:        Pipenv documentation
%description -n %{name}-doc
Documentation for Pipenv


%prep
%autosetup -p1 -n %{name}-%{upstream_version}

tar -xf %{SOURCE1} --strip-components 1 -C tests/pypi

# this goes together with patch4
rm pipenv/patched/notpip/_vendor/certifi/*.pem

# Remove python2 parts because they fail bytecompilation
rm -rf pipenv/patched/yaml2/

# Remove packages that are already packaged for Fedora from vendor directory
UNBUNDLED="appdirs attr cached_property cerberus click colorama distlib docopt first chardet iso8601 jinja2 markupsafe packaging parse pexpect ptyprocess pyparsing dotenv requests certifi idna urllib3 semver shellingham six toml yarg plette pipreqs pipdeptree"

# issue: for loop below doesn't handle multiple imports in one line
# properly. There might be case when library is still not unbundled
# but is not imported from vendor directory.
# diff of pyenv.py:
#  265   │ -from .vendor import attr, delegator
#  266   │ +import attr, delegator
# So we unpack such import statements into multiple lines first:
while matches=$(grep -Elr 'from (\.?pipenv)?\.vendor import ([^,]+), (.+)'); do
  sed -Ei 's/from (\.?pipenv)?\.vendor import ([^,]+), (.+)/from \1.vendor import \2\nfrom \1.vendor import \3/g' $matches
done

for pkg in ${UNBUNDLED[@]}; do
  find pipenv/* tests/* -not -path '*/\.git*' -type f -exec sed -i -E \
  -e "s/from (pipenv)?\.vendor\.${pkg}(\.\S+)? import/from ${pkg}\2 import/" \
  -e "s/^import (pipenv)?\.vendor\.${pkg}(\.\S+)?$/import ${pkg}\2/" \
  -e "s/from (pipenv)?\.vendor import ${pkg}(\.\S+)?$/import ${pkg}\2/" \
  -e "s/(pipenv)?\.vendor\.${pkg}(\.\S+)?($|\s)/${pkg}\2\3/g" {} \;
done

_vendordir="pipenv/vendor/"

for pkg in ${UNBUNDLED[@]}; do
  if [ -d $_vendordir$pkg ]; then
    rm -r $_vendordir$pkg
  elif [ -f $_vendordir$pkg.py ]; then
    rm $_vendordir$pkg".py"
  else
    echo 'Unbundling error:' $pkg 1>&2
    exit 1
  fi
  rm -rf $_vendordir$pkg".LICENSE"*
  rm -rf $_vendordir${pkg/_/-}".LICENSE"*

  if grep -rE "( |\.)vendor\.$pkg" pipenv; then
    echo 'Unbundling error:' $pkg 1>&2
    exit 1
  fi
done

# Remove setup_requires, as we cannot install invoke
sed -i /setup_requires/d setup.py


%build
%py3_build
# generate html docs
export PYTHONPATH=$PWD/build/lib
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
rm -rf html/_sources/


%install
%py3_install
# Remove shebang lines from scripts in project directory
grep "/usr/bin/env python" -lR %{buildroot}%{python3_sitelib}/%{name}| xargs sed -i '1d'


%check
# dirty dirty hack (TODO find a better way)
# for the tests to run, we need to set PYTHONPATH to something that:
#   - has our pipenv (%%{buildroot}%%{python3_sitelib})
#   - has our unbundled deps (%%{python3_sitelib} and %%{python3_sitearch})
#   - doesn't have pip (venv installed pips may have different API)
#   - doesn't have requests (a test uninstalls it and checks it)
# (even externally run pythons read PYTHONPATH and use modules from it)
mkdir check_pythonpath
ln -sf %{buildroot}%{python3_sitelib}/* %{python3_sitelib}/* %{python3_sitearch}/* check_pythonpath/
unlink check_pythonpath/pip
unlink check_pythonpath/pip-*info
unlink check_pythonpath/__pycache__
mkdir check_pythonpath/__pycache__
ln -sf %{python3_sitelib}/__pycache__/* %{python3_sitearch}/__pycache__/* check_pythonpath/__pycache__/

# we also make sure "python" exists and means something
mkdir check_path
%if %{with python2_tests}
ln -s %{__python2} check_path/python
%else
ln -s %{__python3} check_path/python
%endif
test -f %{_bindir}/virtualenv || ln -s %{_bindir}/virtualenv-3 check_path/virtualenv

export PATH=$PWD/check_path:$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PWD/check_pythonpath:$PWD/tests/pytest-pypi
export PYPI_VENDOR_DIR="$(pwd)/tests/pypi/"

# There are 2 types of tests: unit and integration:
# - integration tests require internet and are disabled
# - unit tests that need network are disabled
pytest-3 -m "not needs_internet" -vv -s tests/unit

rm -rf check_pythonpath check_path


%files
%license LICENSE
# To regenerate list of licenses, use:
#  $ ./license-helper.py --bundled-modules bundled-licenses \
#                        --sources <directory created by fedpkg prep> \
#                        --list-license-files
# Keep this list alphabetically sorted
%license %{python3_sitelib}/%{name}/patched/crayons.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/appdirs.LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/certifi/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/chardet/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/contextlib2.LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distro.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/html5lib/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/idna/LICENSE.rst
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/ipaddress.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/msgpack/COPYING
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pep517/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/progress/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pyparsing.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pytoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/retrying.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/six.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/webencodings/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/piptools/LICENSE
%license %{python3_sitelib}/%{name}/patched/safety/LICENSE
%license %{python3_sitelib}/%{name}/patched/yaml3/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/enum/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/functools_lru_cache.LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/shutil_get_terminal_size/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/weakref.LICENSE
%license %{python3_sitelib}/%{name}/vendor/click_completion/LICENSE
%license %{python3_sitelib}/%{name}/vendor/click_didyoumean/LICENSE
%license %{python3_sitelib}/%{name}/vendor/contextlib2.LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/dateutil/LICENSE
%license %{python3_sitelib}/%{name}/vendor/delegator.py.LICENSE
%license %{python3_sitelib}/%{name}/vendor/dparse/LICENSE
%license %{python3_sitelib}/%{name}/vendor/funcsigs/LICENSE
%license %{python3_sitelib}/%{name}/vendor/importlib_metadata/LICENSE
%license %{python3_sitelib}/%{name}/vendor/importlib_resources/LICENSE
%license %{python3_sitelib}/%{name}/vendor/more_itertools/LICENSE
%license %{python3_sitelib}/%{name}/vendor/orderedmultidict/LICENSE.md
%license %{python3_sitelib}/%{name}/vendor/passa/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pathlib2/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/pep517/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pip_shims/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pythonfinder/LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/pythonfinder/_vendor/pep514tools/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pythonfinder/pep514tools.LICENSE
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/resolvelib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/scandir.LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/tomlkit/LICENSE
%license %{python3_sitelib}/%{name}/vendor/vistir/LICENSE
%license %{python3_sitelib}/%{name}/vendor/yaspin/LICENSE
%license %{python3_sitelib}/%{name}/vendor/zipp.LICENSE
%doc README.md NOTICES CHANGELOG.rst HISTORY.txt
%{_bindir}/pipenv
%{_bindir}/pipenv-resolver
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{upstream_version}-*.egg-info

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Tue Aug 25 2020 Tomas Orsava <torsava@redhat.com> - 2020.8.13-1
- Rebase to a new upstream version (#1868686)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Tomas Orsava <torsava@redhat.com> - 2020.6.2-1
- Rebase to a new upstream version (#1842795)

* Thu May 28 2020 Tomas Orsava <torsava@redhat.com> - 2020.5.28-1
- Rebase to a new final upstream version (#1829161)

* Thu Apr 30 2020 Tomas Orsava <torsava@redhat.com> - 2020.4.1~b2-1
- Rebase to a new beta version 2 (#1829161)
- Remove upstreamed patches

* Thu Apr 30 2020 Tomas Orsava <torsava@redhat.com> - 2020.4.1~b1-1
- Rebase to a new beta version (#1829161)
  - Added an upstream patch to not fallback to python unconstrained version
- Fixed unbundling machinery, tomlkit was partially unbundled by mistake
- Added helper script for handling bundled licenses
- Add to files new and missing LICENSE files
- Re-bundled:
  - pip_shims
  - pythonfinder
  - yaspin
  - vistir

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-12
- Keep pathlib2, scandir, click-completion and backports.* bundled (#1767003)
- Keep tomlkit bundled for the same reason

* Fri Oct 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 2018.11.26-11
- Devendored: yaspin vistir pythonfinder plette pipreqs pipdeptree pip_shims tomlkit

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-7
- Require which (#1688145)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-5
- Fix a fix of unbundling of packaging (sorry)

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-4
- Fix unbundling of packaging
- Fixes https://github.com/pypa/pipenv/issues/3469

* Wed Jan  9 2019 Owen Taylor <otaylor@redhat.com> - 2018.11.26-3
- Fix pexpect import for compatibility mode of pipenv shell

* Wed Dec 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-2
- Use the system level root certificate instead of the one bundled in certifi

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-1
- Update to 2018.11.26 (bugfixes only)

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.14-1
- Update to 2018.11.14 (#1652091)
- Should fix incompatibility with pip (#1651317)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-2
- Correct the name of bundled dotenv to python-dotenv

* Fri Jul 27 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-1
- Update to 2018.7.1 (#1609432)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-3
- Do not require pathlib2, it's intended for Python < 3.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-2
- Rebuilt for Python 3.7
- Add patch for patched/bundled prettytoml to work with 3.7

* Fri Apr 13 2018 Michal Cyprian <mcyprian@redhat.com> - 11.10.4-1
- Initial package.
