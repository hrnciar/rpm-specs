%global pypi_name spectrographic

Name: %{pypi_name}
Summary: Turn an image into sound whose spectrogram looks like the image
License: MIT

Version: 0.9.3
Release: 3%{?dist}

URL: https://github.com/LeviBorodenko/%{pypi_name}
Source0: %{pypi_source}

BuildRequires: python3-devel
BuildRequires: python3-pyscaffold
BuildRequires: python3-setuptools >= 38.3
BuildRequires: python3-sphinx

# These aren't strictly required, but sphinx complains
# and yells warnings about failed imports when they're not installed
BuildRequires: python3-pillow
BuildRequires: python3-simpleaudio
BuildRequires: python3-wavio

BuildArch: noarch


%description
Turn any image into a sound whose spectrogram looks like the image!

Most sounds are intricate combinations of many acoustic waves, each having
different frequencies and intensities. A spectrogram is a way to represent
sound by plotting time on the horizontal axis and the frequency spectrum
on the vertical axis. Sort of like sheet music on steroids.

What this tool does is, taking an image and simply interpreting it
as a spectrogram. Therefore, by generating the corresponding sound,
we have embedded our image in a spectrogram.


%package doc
Summary: Documentation for %{pypi_name}
BuildArch: noarch

%description doc
This package contains documentation (in HTML format)
for the %{pypi_name} program.


%prep
%setup -q


%build
%py3_build

cd docs/
make man
make html


%install
%py3_install

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 build/sphinx/man/%{name}.1 %{buildroot}%{_mandir}/man1/


%files
%doc AUTHORS.rst CHANGELOG.rst README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/


%files doc
%doc build/sphinx/html/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.3-2
- Build docs with Sphinx and install them

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.3-1
- Initial packaging
