Name:          fritzing-parts
Version:       0.9.3b
Release:       6%{?dist}
Summary:       Parts library for the Fritzing electronic design application

# The overall distribution is licensed as CC-BY-SA (see LICENSE.txt), but
# many individual SVG parts in the svg/ directory are licensed as GPL+;
# please see the fz:attr elements named "dist-license", "use-license", and
# "license-url" under the rdf:RDF section of each SVG document for details.
License:       CC-BY-SA and GPL+

URL:           http://fritzing.org/
Source0:       https://github.com/fritzing/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: fritzing

%description
Fritzing is a free software tool to support designers, artists and hobbyists
to work creatively with interactive electronics. The fritzing-parts package
contains a library of part definitions, including both meta-data and related
graphics.

%prep
%setup -q -b0

# Get rid of git-related files
find . -name placeholder.txt -exec rm -vf {} \;
rm -vf .gitignore

# Get rid of duplicate LICENSE.txt files
find svg -name LICENSE.txt -exec rm -vf {} \;

%build
# Nothing to do.

%install
mkdir -p %{buildroot}%{_datadir}/fritzing/parts

cp -a bins       %{buildroot}%{_datadir}/fritzing/parts
cp -a contrib    %{buildroot}%{_datadir}/fritzing/parts
cp -a core       %{buildroot}%{_datadir}/fritzing/parts
cp -a obsolete   %{buildroot}%{_datadir}/fritzing/parts
cp -a svg        %{buildroot}%{_datadir}/fritzing/parts
cp -a user       %{buildroot}%{_datadir}/fritzing/parts

# This is necessary to avoid a crash in FApplication::runDatabaseService
# where "pdb" is forcefully indexed (causing a crash if missing).
mkdir %{buildroot}%{_datadir}/fritzing/pdb

Fritzing -platform minimal \
  -f  %{buildroot}%{_datadir}/fritzing/parts \
  -db %{buildroot}%{_datadir}/fritzing/parts/parts.db

# Cleanup
rmdir %{buildroot}%{_datadir}/fritzing/pdb

%files
%doc README.md CONTRIBUTING.md
%license LICENSE.txt
%{_datadir}/fritzing

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Ed Marshall <esm@logic.net> - 0.9.3b-1
- Initial separate packaging of Fritzing parts library.
