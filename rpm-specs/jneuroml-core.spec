%global pretty_name NeuroML2

# Upstream used this as the release tag:
# https://github.com/NeuroML/jNeuroML/tags
%global gittag NMLv2.0

%global _description %{expand:
This repository contains the NeuroML 2 Schema, the ComponentType definitions in
LEMS and a number of example files in NeuroML 2 and LEMS files for running
simulations.

For more details on LEMS and NeuroML 2 see:

Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris
Marin, Eugenio Piasini and R. Angus Silver, LEMS: A language for expressing
complex biological models in concise and hierarchical form and its use in
underpinning NeuroML 2, Frontiers in Neuroinformatics 2014,
doi:10.3389/fninf.2014.00079
}

Name:           jneuroml-core
Version:        1.6.1
Release:        1%{?dist}
Summary:        The NeuroML 2 Schema and ComponentType definitions in LEMS

License:        LGPLv3
URL:            https://github.com/NeuroML/%{pretty_name}

Source0:        %{url}/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin

%description %_description

# NO javadocs

%package doc
Summary:        NeuroML2 core documentation and examples
# bootstrap.css file is ASL 2.0
License:        LGPLv3 and ASL 2.0

%description doc %_description

%prep
%autosetup -n %{pretty_name}-%{gittag}

# Remove currently unused omv/omt files
rm -fv LEMSexamples/test/.test*


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.lesser
%doc README.md CONTRIBUTING.md

%files doc
%license LICENSE.lesser
%doc HISTORY.md
%doc examples docs Schemas LEMSexamples


%changelog
* Thu May 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.1-1
- Update as per review comments: #1828079
- Remove unneeded file listing
- Remove unused validation files
- Update license for doc subpackage

* Sun Apr 26 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.1-1
- Initial build
