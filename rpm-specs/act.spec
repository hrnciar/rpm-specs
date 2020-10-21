Name:           act
%global lname   AutomaticComponentToolkit
%global goipath github.com/Autodesk/%{lname}
Version:        1.6.0
Release:        2%{?dist}
Summary:        Automatic Component Toolkit
License:        BSD

%{?gometa}
%{?!gometa:BuildRequires: /usr/bin/go}

URL:            https://%{goipath}
Source0:        %{url}/archive/v%{version}/%{lname}-%{version}.tar.gz

%description
The Automatic Component Toolkit (ACT) is a code generator that takes an
instance of an Interface Description Language file and generates a thin
C89-API, implementation stubs and language bindings of your desired software
component.

%prep
%autosetup -n %{lname}-%{version}

%build
%{?!gobuild:%global gobuild go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x}
%gobuild -o act Source/*.go

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -vp act %{buildroot}%{_bindir}/


%files
%doc README.md
%license LICENSE.md
%{_bindir}/act

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-1
- Initial package (#1819148)
