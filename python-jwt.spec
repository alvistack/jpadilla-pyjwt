%global debug_package %{nil}

Name: python-jwt
Epoch: 100
Version: 2.3.0
Release: 1%{?dist}
BuildArch: noarch
Summary: JSON Web Token implementation in Python
License: MIT
URL: https://github.com/jpadilla/pyjwt/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-PyJWT
Summary: JSON Web Token implementation in Python
Requires: python3
Requires: python3-cryptography >= 3.3.1
Provides: python3-jwt = %{epoch}:%{version}-%{release}
Provides: python3dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jwt) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-PyJWT
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%files -n python%{python3_version_nodots}-PyJWT
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-PyJWT
Summary: JSON Web Token implementation in Python
Requires: python3
Requires: python3-cryptography >= 3.3.1
Provides: python3-jwt = %{epoch}:%{version}-%{release}
Provides: python3dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jwt) = %{epoch}:%{version}-%{release}

%description -n python3-PyJWT
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%files -n python3-PyJWT
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?fedora_version} >= 33
%package -n python3-jwt
Summary: JSON Web Token implementation in Python
Requires: python3
Requires: python3-cryptography >= 3.3.1
Provides: python3-jwt = %{epoch}:%{version}-%{release}
Provides: python3dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jwt) = %{epoch}:%{version}-%{release}

%description -n python3-jwt
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%package -n python3-jwt+crypto
Summary: JSON Web Token implementation in Python
Requires: python3-cryptography >= 3.3.1

%description -n python3-jwt+crypto
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%files -n python3-jwt
%license LICENSE
%{python3_sitelib}/*

%files -n python3-jwt+crypto
%license LICENSE
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?fedora_version} >= 33)
%package -n python3-jwt
Summary: JSON Web Token implementation in Python
Requires: python3
Requires: python3-cryptography >= 3.3.1
Provides: python3-jwt = %{epoch}:%{version}-%{release}
Provides: python3dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jwt) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jwt = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jwt) = %{epoch}:%{version}-%{release}

%description -n python3-jwt
A Python implementation of JSON Web Token draft 01. This library
provides a means of representing signed content using JSON data
structures, including claims to be transferred between two parties
encoded as digitally signed and encrypted JSON objects.

%files -n python3-jwt
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
